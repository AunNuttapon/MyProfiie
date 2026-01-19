from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId

class MongoDBClient:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: dict):
        return self.collection.insert_one(data)

    def find_one(self, query: dict):
        return self.collection.find_one(query)

    def update(self, query: dict, update_data: dict):
        return self.collection.update_one(query, {"$set": update_data})

    def delete(self, query: dict):
        return self.collection.delete_one(query)

class Vote(BaseModel):
    name: str
    count: int

class VoteService:
    def __init__(self, db_client: MongoDBClient):
        self.db_client = db_client

    def create_vote(self, vote: Vote):
        return self.db_client.insert(vote.dict())

    def get_vote(self, vote_id: str):
        return self.db_client.find_one({"_id": ObjectId(vote_id)})

    def update_vote(self, vote_id: str, vote: Vote):
        return self.db_client.update({"_id": ObjectId(vote_id)}, vote.dict())

    def delete_vote(self, vote_id: str):
        return self.db_client.delete({"_id": ObjectId(vote_id)})

app = FastAPI()

mongo_client = MongoDBClient("mongodb://localhost:27017/", "votes", "votes")
vote_service = VoteService(mongo_client)

@app.post("/votes/")
async def create_vote(vote: Vote):
    result = vote_service.create_vote(vote)
    return {"id": str(result.inserted_id), "name": vote.name, "count": vote.count}

@app.get("/votes/{vote_id}")
async def read_vote(vote_id: str):
    vote = vote_service.get_vote(vote_id)
    if vote:
        return {"id": str(vote["_id"]), "name": vote["name"], "count": vote["count"]}
    else:
        raise HTTPException(status_code=404, detail="Vote not found")

@app.put("/votes/{vote_id}")
async def update_vote(vote_id: str, vote: Vote):
    result = vote_service.update_vote(vote_id, vote)
    if result.modified_count == 1:
        return {"id": vote_id, "name": vote.name, "count": vote.count}
    else:
        raise HTTPException(status_code=404, detail="Vote not found")

@app.delete("/votes/{vote_id}")
async def delete_vote(vote_id: str):
    result = vote_service.delete_vote(vote_id)
    if result.deleted_count == 1:
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=404, detail="Vote not found")
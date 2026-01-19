import requests

class Pokemon:
    base_url = "https://pokeapi.co/api/v2/"

    def __init__(self, name):
        self.name = name
        self.id = None
        self.height = None
        self.weight = None

    def fetch_data(self):
        url = f"{self.base_url}pokemon/{self.name}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            self.id = pokemon_data["id"]
            self.height = pokemon_data["height"]
            self.weight = pokemon_data["weight"]
        else:
            print(f"Failed to retrieve data: {response.status_code}")

    def display_info(self):
        if self.id:
            print(f"Name: {self.name}")
            print(f"Id: {self.id}")
            print(f"Height: {self.height}")
            print(f"Weight: {self.weight}")
        else:
            print(f"No data available for {self.name}")

pikachu = Pokemon("pikachu")
pikachu.fetch_data()
pikachu.display_info()
import { useState } from "react";
import React from "react";
import { FaHeart, FaRegHeart } from "react-icons/fa";

function LikePoke() {
  const [like, setLike] = useState(false);
  const togglelike = () => {
    setLike((check) => !check);
  };
  return (
    <button onClick={togglelike}>{like ? <FaHeart style={{ color: "red" }}/> : <FaRegHeart />}</button>
  );
}

export default LikePoke;

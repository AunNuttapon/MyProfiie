import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import axios from "axios";
import ReactLoading from "react-loading";

// Component
import FavPoke from "./components/FavPoke";

function App() {
  const [poke, setPoke] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [number, setNumber] = useState(1);
  const [fav, setFav] = useState([]);
  useEffect(() => {
    let abortController = new AbortController();

    const loadPoke = async () => {
      try {
        setLoading(true);
        let response = await axios.get(
          `https://pokeapi.co/api/v2/pokemon/${number}`,
          {
            signal: abortController.signal,
          }
        );

        setPoke(response.data);
        setError("");
      } catch (error) {
        setError(`Something went wrong: ${error.message}`);
      } finally {
        setLoading(false);
      }
    };

    loadPoke();

    return () => abortController.abort();
  }, [number]);

  console.log(poke);

  const prevPoke = () => {
    setNumber((number) => number - 1);
  };

  const nextPoke = () => {
    setNumber((number) => number + 1);
  };

  const addfav = () => {
    setFav((oldState) => [...oldState, poke]);
  };

  return (
    <>
      <div className="block max-w-5xl p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
        <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2">
          <div>
            {loading ? 
              <ReactLoading
                type="spin"
                color="white"
                height={"20%"}
                width={"20%"}
              />
              :
                          <>
                <h1>
                  No.{number} {poke?.name}
                </h1>
                <br />
                <button onClick={addfav}>Add</button>
                {poke?.sprites?.other?.home?.front_default ? (
                  <img
                    src={poke.sprites.other.home.front_default}
                    alt={poke.name}
                  />
                ) : (
                  <p>Image not available</p>
                )}
                <ul>
                  {poke?.abilities && Array.isArray(poke.abilities) ? (
                    poke.abilities.map((abil, idx) => (
                      <li key={idx}>{abil.ability.name}</li>
                    ))
                  ) : (
                    <li>No abilities available</li>
                  )}
                </ul>
                <br />
                <button onClick={prevPoke}>Previous</button>
                <button onClick={nextPoke}>Next</button>
              </>
            }
          </div>
          <div>
            <h1>My Pokemon</h1>
            {fav.length > 0 ? <FavPoke fav={fav} /> : <div className='flex h-full justify-center items-center'><p>No Pokemon</p></div>}
          </div>
        </div>
      </div>
    </>
  );
}

export default App;

import Search from "@assets/Navbar/search.svg";
import { useEffect, useState } from "react";
import useServiceOptions from "../../services/useServiceOptions";

function SearchNavbar(){
    const {handleOptions} = useServiceOptions();
    const [search, setsearch] = useState("");
    const [options, setoptions] = useState([]);

    const handleSubmit = (event) => {
      event.preventDefault();
      alert(search);
    }
    const setterOptions = (data) =>{
        setoptions(data);
    }

    useEffect(() => {
        handleOptions(setterOptions);
    }, [])
    
    
    return (
      <form onSubmit={handleSubmit}>
        <div className="flex py-1 px-4 border-[1px] border-black rounded-3xl gap-1 ">
          <input type="text" list="myOptions" value={search} onChange={(event) => setsearch(event.target.value)} className="w-full  xl:w-[350px] rounded-lg border-none outline-none font-rubik" placeholder="Buscar"/>
          <button type="submit">
            <img src={Search} alt="search_logo" className="size-6 cursor-pointer"/>
          </button>
        </div>
      </form>
    );
  }

export default SearchNavbar;
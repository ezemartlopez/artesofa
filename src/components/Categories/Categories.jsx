import Sofas from "@assets/Categories/sofas.png";
import Esquineros from "@assets/Categories/esquineros.png";
import Muebles from "@assets/Categories/muebles.png";
import Rinconeros from "@assets/Categories/rinconeros.png";

function Categories() {
  return (
<div className="xl:h-[750px] sm:h-[1500px] h-[1300px] w-full">
  <div className="grid h-full w-full xl:grid-cols-12 grid-cols-1 gap-8">

    <div className="h-full xl:col-span-5 col-span-1">
      <a href="/sofas/" target="_blank" className="w-full">
        <div className=" h-full relative cursor-pointer group overflow-hidden">
          <img src={Sofas} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40 group-hover:bg-slate-700 transition-all duration-500">
            <span className="sm:text-[70px] text-[50px] text-white font-rubik font-bold z-10">SOFAS</span>
          </div>
        </div>
      </a>
    </div>

    <div className="xl:col-span-7 col-span-1 grid grid-rows-2 gap-8">

      <div>
        <a href="/esquineros/" target="_blank">
          <div className="w-full h-full relative cursor-pointer group overflow-hidden">
            <img src={Esquineros} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
            <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40 group-hover:bg-slate-700 transition-all duration-500">
              <span className="sm:text-[70px] text-[40px] text-white font-rubik font-bold z-10">ESQUINEROS</span>
            </div>
          </div>
        </a>
      </div>

      <div className="grid sm:grid-cols-2 sm:grid-rows-1 grid-cols-1 grid-rows-2 gap-8">

        <div>
          <a href="/muebles/" target="_blank">
            <div className="w-full h-full relative cursor-pointer group overflow-hidden">
              <img src={Muebles} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
              <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40 group-hover:bg-slate-700 transition-all duration-500">
                <span className="md:text-[50px] sm:text-[45px] text-[40px] text-white font-rubik font-bold z-10">MUEBLES</span>
              </div>
            </div>
          </a>
        </div>

        <div>
          <a href="/rinconeros/" target="_blank">
            <div className="w-full h-full relative cursor-pointer group overflow-hidden">
              <img src={Rinconeros} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
              <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40 group-hover:bg-slate-700 transition-all duration-500">
                <span className="md:text-[50px] sm:text-[45px] text-[40px] text-white font-rubik font-bold z-10">RINCONEROS</span>
              </div>
            </div>
          </a>
        </div>

      </div>
    </div>
  </div>
</div>

  );
}

export default Categories;
/*
    <div className="h-[750px] w-full">
      <div className="grid h-full w-full grid-cols-12 gap-8">
        <div className="bg-red-300 h-full col-span-5">
          <div className="w-full h-full relative group overflow-hidden">
            <img src={Sofas} alt="categorie_sofa" className="absolute w-full h-full object-cover transition-opacity duration-600 group-hover:scale-105"/>
            <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40  transition-opacity duration-600">
              <span className="text-[70px] text-white font-rubik font-bold z-10">SOFAS</span>
            </div>
            </div>
            </div>
    
            <div className="col-span-7 grid grid-rows-2 gap-8">
              <div className="bg-blue-400">
                <div className="w-full h-full relative group overflow-hidden">
                  <img src={Esquineros} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105"/>
                  <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40">
                    <span className="text-[70px] text-white font-rubik font-bold z-10">ESQUINEROS</span>
                  </div>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-8">
                <div className="bg-green-300">
                  <div className="w-full h-full relative group overflow-hidden">
                    <img src={Muebles} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105"/>
                    <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40">
                      <span className="text-[50px] text-white font-rubik font-bold z-10">MUEBLES</span>
                    </div>
                  </div>
                </div>
                <div className="bg-orange-300">
                  <div className="w-full h-full relative group overflow-hidden">
                    <img src={Rinconeros} alt="categorie_sofa" className="absolute w-full h-full object-cover group-hover:scale-105"/>
                    <div className="absolute z-10 w-full h-full flex justify-center items-center bg-slate-500 bg-opacity-25 group-hover:bg-opacity-40">
                      <span className="text-[50px] text-white font-rubik font-bold z-10">RINCONEROS</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
*/
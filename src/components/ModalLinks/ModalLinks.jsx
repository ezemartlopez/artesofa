import Xmark from "@assets/Xmark/Xmark.svg";
import { useEffect, useState } from "react";
import ModalLeft from "../Modal/ModalLeft";
import SearchNavbar from "../SearchNavbar/SearchNavbar";
  
function ModalLinks({ condition, toggle }) {
  const [show, setShow] = useState(false);
  const closeModal = () =>{
    setShow(false);
    setTimeout(()=>{toggle()},300);
  }
  
  useEffect(() => {
    if(condition){
      setTimeout(()=>{setShow(true)},100);
    }
    
  }, [condition])
  
  return (
            <ModalLeft condition={condition} closeModal={closeModal} show={show}>
              <div className="relative bg-white z-20 rounded-xl h-full w-screen sm:w-[350px] px-4 flex flex-col justify-start overflow-y-auto">
                {/* Title */}
                <div className="w-full py-[20px] rounded-xl flex justify-end items-center">
                  <div className="size-[25px] rounded-full hover:bg-slate-200 flex justify-center items-center cursor-pointer" onClick={closeModal}>
                    <img src={Xmark} alt="close" className="size-[20px]" />
                  </div>
                </div>
                {/* Body */}
                <div className="w-full flex-grow overflow-y">
                  {/* Body Content */}
                  
                  {/* 
                  <div className="xl:hidden inline-block">
                    <SearchNavbar/>
                  </div>
                  */}
                  <ul className="w-full flex flex-col gap-4 mt-4">
                    <li><a href="/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Inicio</a></li>
                    <li><a href="/sofas/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Sofás</a></li>
                    <li><a href="/sofas-cama/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Sofás Cama</a></li>
                    <li><a href="/esquineros/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Esquineros</a></li>
                    <li><a href="/rinconeros/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Rinconeros</a></li>
                    <li><a href="/precio-especial/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Precio Especial</a></li>
                    <li><a href="/individuales/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Individuales</a></li>
                    <li><a href="/muebles/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Muebles</a></li>
                    <li><a href="/complemento/" className="block rounded-md pl-2 text-rubik text-lg font-bold hover:text-black/50">Complementos</a></li>
                  </ul>
                </div>
                {/* Base */}
                <div className="sticky">
                  Base fija
                </div>
                {/* Fin Base */}
              </div>
            </ModalLeft>

  );
}

export default ModalLinks;
/*
Inicio
Sofás
Esquineros
Rinconeros
Sofás cama
Precio Especial
Individuales
Muebles
Complementos
*/
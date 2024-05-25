import Xmark from "@assets/Xmark/Xmark.svg";
import { useEffect, useState } from "react";
import Modal from "../Modal/Modal";
import useCartShop from "@hooks/useCartShop";
  
function ItemProduct({product}){
  return (
    <div className="py-1 flex">
      <div className="w-auto">
        <img src={product.url_image} alt="" className="h-[90px] w-[110px]"/> 
      </div>
      <div className="flex-grow flex flex-col pl-6 justify-between">
        <span className="">{product.name}</span>
        <span className="font-bold">${product.price}</span>
        <div className="w-min rounded-full p-1 border border-slate-300/80 flex">
          <span className="size-8 rounded-full font-bold text-white bg-orange-400 flex justify-center items-center cursor-pointer">-</span>
          <span className="h-8 w-10 flex justify-center items-center">{product.count}</span>
          <span className="size-8 rounded-full font-bold text-white bg-orange-400 flex justify-center items-center cursor-pointer">+</span>
        </div>
        
      </div>
    </div>
  );
}

function ModalCartShop({ condition, toggle }) {
  const [show, setShow] = useState(false);
  const {cartList} = useCartShop();
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
            <Modal condition={condition} closeModal={closeModal} show={show}>
              <div className="relative bg-white z-20 rounded-xl h-full w-screen sm:w-[650px] px-8 flex flex-col justify-start overflow-y-auto">
                {/* Title */}
                <div className="w-full min-h-[100px] rounded-xl flex justify-between items-center">
                  <span className="font-rubik text-[22px] font-semibold">Carrito de Compras</span>
                  <div className="size-[40px] rounded-full hover:bg-slate-200 flex justify-center items-center cursor-pointer" onClick={closeModal}>
                    <img src={Xmark} alt="close" className="size-[25px]" />
                  </div>
                </div>
                {/* Body */}
                <div className="w-full flex-grow overflow-y">
                  {/* Body Content */}
                  {cartList.length === 0? <p>No hay elementos a mostrar</p>: null}
                  {cartList.map((product, index) => (<ItemProduct product={product} key={index}/>))}
                </div>
                {/* Base */}
                <div className="sticky">
                  <div className="w-full min-h-[100px]">
                    <div className="w-full flex justify-between">
                      <span className="font-rubik text-[22px] font-bold text-orange-500">Total:</span>
                      <span className="font-rubik text-[22px] font-bold text-orange-500">$987.800,00</span>
                    </div>
                    <div className="w-full flex justify-end">
                      <span className="font-rubik text-lg font-bold">O hasta 6 cuotas de $164.633,33</span>
                    </div>
                    <div className="py-[10px]">
                      <button className="w-full py-[10px] font-rubik text-base text-white hover:text-orange-500 border-[2px] border-orange-500 bg-orange-500 hover:bg-white rounded-full tracking-[5px]">INICIAR COMPRA</button>
                    </div>
                    <div className="w-full pb-[20px] flex justify-center">
                      <span className="font-rubik hover:text-orange-500 cursor-pointer" onClick={closeModal}>Ver más productos</span>
                    </div>
                  </div>
                </div>
                {/* Fin Base */}
              </div>
            </Modal>

  );
}

export default ModalCartShop;

import Xmark from "@assets/Xmark/Xmark.svg";
import { useEffect, useState } from "react";
import Modal from "../Modal/Modal";

function formatNumberWithDots(numberString) {
  // Convertir el string a un número
  const number = parseFloat(numberString);
  // Verificar si la conversión fue exitosa
  if (isNaN(number)) {
      throw new Error("Input is not a valid number");
  }
  // Formatear el número con puntos como separadores de miles
  return number.toLocaleString('de-DE');
}


function ItemProduct({product, removeProductById, incrementProductCount, decrementProductCount}){
  return (
    <div className="py-1 relative flex bg-green-400">
      <div className="absolute right-3 h-full flex flex-col justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" onClick={() => removeProductById(product.id)} 
          className="size-10 p-1 stroke-black stroke-1 cursor-pointer rounded-full border hover:border-slate-500 ">
          <path d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
        </svg>  
      </div>
      <div className="w-auto">
        <img src={product.url_image} alt="" className="h-[80px] w-[100px] sm:h-[100px] sm:w-[120px] object-cover"/> 
      </div>
      <div className="flex-grow flex flex-col pl-6 justify-between">
        <span className="sm:text-base text-sm">{product.name}</span>
        <span className="font-bold">${formatNumberWithDots(product.price)}</span>
        <div className="w-min rounded-full p-1 border border-slate-300/80 flex">
          <span onClick={() => decrementProductCount(product.id)} className="sm:size-8 size-6 rounded-full font-bold text-white bg-orange-400 flex justify-center items-center cursor-pointer">-</span>
          <span className="h-full w-10 flex justify-center items-center">{product.count}</span>
          <span onClick={() => incrementProductCount(product.id)} className="sm:size-8 size-6 rounded-full font-bold text-white bg-orange-400 flex justify-center items-center cursor-pointer">+</span>
        </div>
        
      </div>
    </div>
  );
}

function ModalCartShop({ condition, toggle, products, removeProductById, incrementProductCount, decrementProductCount}) {
  const [show, setShow] = useState(false);
  const montoTotal = products.reduce((accumulator, item) => accumulator + (item.count *  item.price), 0);
  const total = montoTotal + "";
  const CUOTAS = 6;
  const totalCuotas = (montoTotal / CUOTAS).toFixed(2) + "";
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
                <div className="w-full flex-grow overflow-y-scroll flex flex-col gap-3">
                  {/* Body Content */}
                  {products.length === 0? <p>No hay elementos a mostrar</p>: null}
                  {products.map((product, index) => (<ItemProduct product={product} key={index} removeProductById={removeProductById} incrementProductCount={incrementProductCount} decrementProductCount={decrementProductCount}/>))}
                </div>
                {/* Base */}
                <div className="sticky pt-4">
                  <div className="w-full min-h-[100px]">
                    <div className="w-full flex justify-between">
                      <span className="font-rubik text-[22px] font-bold text-orange-500">Total:</span>
                      <span className="font-rubik text-[22px] font-bold text-orange-500">${formatNumberWithDots(total)}</span>
                    </div>
                    <div className="w-full flex justify-end">
                      <span className="font-rubik sm:text-lg text-sm font-bold">O hasta {CUOTAS} cuotas de ${formatNumberWithDots(totalCuotas)}</span>
                    </div>
                    <div className="py-[15px]">
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

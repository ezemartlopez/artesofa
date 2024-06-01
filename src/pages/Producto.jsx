
const apiUrl = import.meta.env.VITE_API_URL;

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Carousel from "../components/Carousel/Carousel";

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

function Producto() {
  const {id} = useParams();
  const url = apiUrl + "/productos/" + id;
  const [product, setproduct] = useState(null);

  useEffect(() => {
    fetch(url)
    .then(response => response.json())
    .then(data => setproduct(data))
    .catch(error => console.error('Error:', error));
  }, [])
  const imagenes = product? [product["image_primary"], product["image_secondary"]]:[];
  return (
    <>
      <div className="w-full flex flex-col-reverse xl:flex-row pt-4">
        
        <div className="flex-grow px-4 xl:px-8">
            <div className="flex text-sm text-slate-600 gap-2 pt-2">
              <span>Inicio</span>
              <span>{">"}</span>
              <span className="capitalize">{product?.type}</span>
              <span>{">"}</span>
              <span>{product?.name}</span>
            </div>
          <div className="flex flex-col">
            <h1 className="text-4xl font-rubik font-bold py-4">{product?.name}</h1>
            {product?.cash_price? 
            <div className="flex flex-col gap-2 py-1">
              <span className=" text-orange-500 font-rubik font-bold text-[22px]">EFECTIVO: ${formatNumberWithDots(product?.cash_price + "")}</span>
              <span className="font-rubik text-sm">¿Cómo pagar en efectivo/transferencia?</span>
            </div>
            : null}
            <div className="flex flex-col pt-3 gap-1 xl:gap-3">
              <span className="text-black font-rubik font-semibold text-[22px]">LISTA: ${formatNumberWithDots(product?.price + "")}</span>
              <div className="flex gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="size-5 stroke-1 stroke-orange-500">
                  <path d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                </svg>
                <span className="font-rubik text-sm"> Hasta <span className="text-orange-500 text-[15px] font-medium">4</span> cuotas SIN interés con <span className="text-orange-500 text-[15px] font-medium">tarjeta de DÉBITO</span></span>
              </div>
              <div className="flex gap-1">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="size-5 stroke-1 stroke-orange-500">
                  <path d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z" />
                </svg>
                <span className="font-rubik text-sm"><span className="text-orange-500 text-[15px] font-medium">6 cuotas sin interés</span> de $94.633,33</span>
              </div>
              <span className="text-xs font-rubik text-orange-500">Ver más detalles</span>
              <div className="w-full pt-2">
                <div className="">
                  
                </div>
                <button className="uppercase border-2 font-rubik font-medium transition-colors duration-500 border-orange-500 bg-orange-500 text-white w-full py-2 rounded-2xl hover:bg-white hover:text-orange-500">agregar al carrito</button>
              </div>
            </div>
          </div>
        </div>
        <div className="xl:w-[1000px] xl:h-[700px] w-full lg:h-[600px] md:h-[500px] sm:h-[400px] h-[350px]">
          <Carousel slides={imagenes} autoSlide={true} cover={true}/>
        </div>
      </div>
    </>
  )
}


export default Producto;
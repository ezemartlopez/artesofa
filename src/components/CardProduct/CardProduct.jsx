/*CONTRATO
{
    name: product.name,
    price: product.price,
    cash_price: product.cash_price,
    image: product.image_primary,
    image_hover: product.image_secondary
}
*/
function ButtonAddCart({handleClick}) {
  return(
  <span className="absolute top-2 right-2 z-10 flex group">
    <span className="flex items-center pl-4 text-white text-sm py-1 px-2 rounded-l-full bg-orange-400 opacity-0 transition-opacity ease-linear duration-300 group-hover:opacity-100">Agregar al carrito</span>
    <span className="size-10  rounded-full flex items-center justify-center bg-orange-400/50 text-white font-semibold text-2xl group-hover:bg-orange-400 transition-colors duration-0 group-hover:rounded-l-none" onClick={handleClick}>+</span>
  </span>
  )
}

function CardProduct({product}) {
  const {name, price, cash_price, image, image_hover, id} = product;
  const cuotes = price / 6;
  const handleClick = () =>{
    console.log(id);
  }
  return (
<div className="font-rubik h-auto w-full border border-gray-200 bg-white shadow-md">
      {/*<!-- Contenedor de la card definida por defecto -->*/}
      <div className="flex h-full w-full flex-col justify-start">
        {/*<!-- Contenedor para la imagen -->*/}
        <div className="relative h-[350px] w-full cursor-pointer sm:flex-grow">
          {/*<span className="absolute size-10 top-2 right-2 rounded-full z-10 flex items-center justify-center  bg-orange-400/50 text-white font-semibold text-2xl hover:bg-orange-400" onClick={handleClick}>+</span>*/}
          <ButtonAddCart handleClick={handleClick}/>
          <img src={image} alt="imagen" className="absolute h-full w-full transform object-cover transition duration-700 ease-in-out" />
          <img src={image_hover} alt="imagen-hover" className="absolute h-full w-full transform object-cover opacity-0 transition duration-700 ease-in-out hover:opacity-100" />
        </div>
        {/*<!-- Contenedor del contenido -->*/}
        <div className="flex h-[130px] w-full flex-col items-center justify-start pt-3">
          <span className="block font-normal">{name}</span>
          <span className="block font-bold text-orange-500">EFECTIVO $ {cash_price}</span>
          <span className="block font-medium">LISTA $ {price}</span>
          <span className="block text-sm">6 cuotas sin interés de $ {cuotes.toFixed(2)}</span>
        </div>
      </div>
    </div>
  );
}

export default CardProduct;
/*
  <div className="h-auto w-full bg-white shadow-md font-rubik border-gray-200 border">
        {/<!-- Contenedor de la card definida por defecto -->/}
        <div className="flex h-full w-full flex-col justify-start">
            {/*<!-- Contenedor para la imagen -->/}
            <div className="w-full sm:flex-grow h-[350px] pt-2" onMouseEnter={mouseEnter} onMouseLeave={mouseLeave}>
                <img src={isHover?image:image_hover}  alt="imagen" className="h-full w-full object-fill" />
            </div>
            {/*<!-- Contenedor del contenido -->/}
            <div className="flex h-[130px] w-full flex-col items-center justify-start pt-3">
                <span className="block font-normal">ITALIANO</span>
                <span className="block font-bold text-orange-500">EFECTIVO $ 450.160,00</span>
                <span className="block font-medium">LISTA $652.700,00</span>
                <span className="block text-sm"> 6 cuotas sin interés de $93.783,33 </span>
            </div>
        </div>
    </div>
    <div class="font-rubik h-auto w-full border border-gray-200 bg-white shadow-md">
      <!-- Contenedor de la card definida por defecto -->
      <div class="flex h-full w-full flex-col justify-start">
        <!-- Contenedor para la imagen -->
        <div class="relative h-[350px] w-full pt-2 sm:flex-grow">
          <img src="https://silloneseuropa.com.ar/wp-content/uploads/2021/08/juani-1.jpg" alt="imagen" class="absolute inset-0 h-full w-full transform object-contain transition duration-300 ease-in-out" />
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwMRPtZp6NkPDJILtr27aD0Y5ZQkLgaUYEgQ&usqp=CAU" alt="imagen-hover" class="absolute inset-0 h-full w-full transform object-contain opacity-0 transition duration-300 ease-in-out hover:opacity-100" />
        </div>
        <!-- Contenedor del contenido -->
        <div class="flex h-[130px] w-full flex-col items-center justify-start pt-3">
          <span class="block font-normal">ITALIANO</span>
          <span class="block font-bold text-orange-500">EFECTIVO $ 450.160,00</span>
          <span class="block font-medium">LISTA $652.700,00</span>
          <span class="block text-sm">6 cuotas sin interés de $93.783,33</span>
        </div>
      </div>
    </div>
*/
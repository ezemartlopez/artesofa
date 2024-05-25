import Logo from "@assets/Navbar/logo.png";
import Carrito from "@assets/Navbar/cart.svg";
import Search from "@assets/Navbar/search.svg";
import Menu from "@assets/Navbar/menu.svg";
import useCartShop from "@hooks/useCartShop";

function Navbar({toggle, navigation}) {
  const {amountProducts} = useCartShop();
  return (
    <div className="w-full shadow-lg">
        <div className="relative flex h-[80px] w-full justify-center bg-white">
            <div className="absolute left-4 h-full w-auto flex justify-center items-center gap-2 z-10">
              <div className="cursor-pointer" onClick={navigation}>
                <img src={Menu} alt="Menu" className="size-8"/>
              </div>
              <div className="hidden xl:inline-block">
                <div className="flex py-1 px-4 border-[1px] border-black rounded-3xl gap-1 ">
                  <input type="text" className="w-[350px] rounded-lg border-none outline-none font-rubik" placeholder="Buscar"/>
                  <img src={Search} alt="search_logo" className="size-6 cursor-pointer"/>
                </div>  
              </div>
              
            </div>

            <div className="h-full w-auto flex justify-center items-center cursor-pointer">
              <a href="/">
                <img src={Logo} alt="imagen_logo" className="h-[60px] object-cover" />
              </a>
            </div>

            <div className="absolute right-4 h-full w-auto flex justify-center items-center">
                <div className="size-[60px] flex justify-center items-center relative cursor-pointer" onClick={toggle}>
                  <img src={Carrito} alt="carrito" className="size-[35px]"/>
                  <span className="bg-orange-500 size-5 rounded-[50%] text-xs text-white flex justify-center items-center absolute right-[5px] top-[5px]">{amountProducts}</span>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Navbar;
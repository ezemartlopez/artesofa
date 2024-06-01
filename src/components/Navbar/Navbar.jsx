import Logo from "@assets/Navbar/logo.png";
import Carrito from "@assets/Navbar/cart.svg";
import Menu from "@assets/Navbar/menu.svg";
//import SearchNavbar from "@components/SearchNavbar/SearchNavbar";

function Navbar({toggle, navigation, cantidad}) {
  return (
    <div className="w-full shadow-lg">
        <div className="relative flex h-[80px] w-full justify-center bg-white">
            <div className="absolute left-4 h-full w-auto flex justify-center items-center gap-2 z-10">
              <div className="cursor-pointer" onClick={navigation}>
                <img src={Menu} alt="Menu" className="size-8"/>
              </div>
              {/** 
              <div className="hidden xl:inline-block">
                <SearchNavbar/>
              </div>
              */}
            </div>

            <div className="h-full w-auto flex justify-center items-center cursor-pointer">
              <a href="/">
                <img src={Logo} alt="imagen_logo" className="h-[60px] object-cover" />
              </a>
            </div>

            <div className="absolute right-4 h-full w-auto flex justify-center items-center">
                <div className="size-[60px] flex justify-center items-center relative cursor-pointer" onClick={toggle}>
                  <img src={Carrito} alt="carrito" className="size-[35px]"/>
                  <span className="bg-orange-500 size-5 rounded-[50%] text-xs text-white flex justify-center items-center absolute right-[5px] top-[5px]">{cantidad}</span>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Navbar;
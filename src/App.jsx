import RouterApp from "./routes/RouterApp";


function App() {
  return (
    <RouterApp></RouterApp>
  )
}

export default App;

/**

import Navbar from "@components/Navbar/Navbar";
import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import WhatsappLogo from "@assets/whatsapp.svg";
import TitleHash from "@components/TitleHash/TitleHash";
import PaymentMethods from "@components/PaymentMethods/PaymentMethods";
import Categories from "@components/Categories/Categories";
import InstagramLink from "@components/InstagramLink/InstagramLink";
import Footer from "@components/Footer/Footer";
import { useState } from "react";
import Slider from "@components/Slider/Slider";
import ModalCartShop from "@components/ModalCartShop/ModalCartShop";
import ModalLinks from "@components/ModalLinks/ModalLinks";

function useShoppingCart(){
  const [visibleCart, setvisiblecart] = useState(false);
  const toggleCart = () => {setvisiblecart(!visibleCart)};
  return {visibleCart, toggleCart};
}
function useLinks(){
  const [visibleLinks, setvisiblelinks] = useState(false);
  const toggleLinks = () => {setvisiblelinks(!visibleLinks); console.log("abri links");};
  return {visibleLinks, toggleLinks};
}

export default function App() {
  const {visibleCart, toggleCart} = useShoppingCart();
  const {visibleLinks, toggleLinks} = useLinks();

  return (
  
  <div className="relative max-w-screen h-screen ">
    {<div className={"relative max-w-screen h-screen " + (visibleCart || visibleLinks?"":"")}> }
    <ModalLinks condition={visibleLinks} toggle={toggleLinks}/>
    <ModalCartShop condition={visibleCart} toggle={toggleCart}/>

    <div className="flex flex-col justify-start px-4">
      <div className="w-full h-full relative">
        {<div class="fixed inset-0 z-10 flex max-h-full max-w-full items-center justify-center overflow-hidden bg-black bg-opacity-50 text-white">Prueba de codigo superpuesto</div>}
        <header className="sticky top-0 min-h-20 w-full block z-20">
          <nav className="w-full">
            <Navbar toggle={toggleCart} navigation={toggleLinks}></Navbar>
          </nav>
        </header>

        <main className="h-auto w-full block">
          <div className="w-full h-full">
            <Slider/>
            <ProductsContainer/>
            <TitleHash/>
            <Categories/>
            <PaymentMethods/>
            <InstagramLink/>
          </div>
        </main>
        
        <footer className="min-h-[100px] w-full block">
          <Footer/>
        </footer>

        <div className="sticky bottom-0 right-0 min-h-[50px] w-full flex items-center justify-center">
          <div className="w-full h-full flex justify-end">
            {/*<span>Bases y condiciones de la aplicacion</span>}
            <div className="size-10 bg-green-500 rounded-full shadow-xl flex justify-center items-center">
              <img src={WhatsappLogo} alt="whatsapp" className="size-6"/>
            </div>
          </div>
        </div>  

      </div>
    </div>
  </div>
  );
}

 */
import Navbar from "@components/Navbar/Navbar";
import WhatsappLogo from "@assets/whatsapp.svg";
import Footer from "@components/Footer/Footer";
import { useEffect, useRef, useState } from "react";
import ModalCartShop from "@components/ModalCartShop/ModalCartShop";
import ModalLinks from "@components/ModalLinks/ModalLinks";
import { Outlet } from "react-router-dom";
import Message from "@components/Message/Message";

function useShoppingCart(){
  const [visibleCart, setvisiblecart] = useState(false);
  const toggleCart = () => {setvisiblecart(!visibleCart)};
  return {visibleCart, toggleCart};
}
function useLinks(){
  const [visibleLinks, setvisiblelinks] = useState(false);
  const toggleLinks = () => {setvisiblelinks(!visibleLinks);};
  return {visibleLinks, toggleLinks};
}

export default function Base({cantidad, products, removeProductById, incrementProductCount, decrementProductCount, messages}) {
  const {visibleCart, toggleCart} = useShoppingCart();
  const {visibleLinks, toggleLinks} = useLinks();
  const [scrollPosition, setScrollPosition] = useState(0);
  const scrollableRef = useRef(null);

  useEffect(() => {
    if (visibleLinks || visibleCart) {
      // Guardar la posición del scroll
      if (scrollableRef.current) {
        setScrollPosition(scrollableRef.current.scrollTop);
        // Deshabilitar el overflow-y
        scrollableRef.current.style.overflowY = 'hidden';
      }
    } else {
      // Restaurar la posición del scroll
      if (scrollableRef.current) {
        scrollableRef.current.style.overflowY = 'auto';
        scrollableRef.current.scrollTop = scrollPosition;
      }
    }
  }, [visibleCart, visibleLinks, scrollPosition]);

  

  return (
    <div ref={scrollableRef} className={"relative max-w-screen h-screen " + (visibleCart || visibleLinks?"overflow-y-hidden":"")}> 
  
 {/* <div className="relative max-w-screen h-screen ">*/}
    <ModalLinks condition={visibleLinks} toggle={toggleLinks}/>
    <ModalCartShop condition={visibleCart} toggle={toggleCart} products={products} removeProductById={removeProductById} incrementProductCount={incrementProductCount} decrementProductCount={decrementProductCount}/>

    <div className="flex flex-col justify-start px-4">
      <div className="w-full h-full relative">
        {/*<div class="fixed inset-0 z-10 flex max-h-full max-w-full items-center justify-center overflow-hidden bg-black bg-opacity-50 text-white">Prueba de codigo superpuesto</div>*/}
        <header className="sticky top-0 min-h-20 w-full block z-20">
          <nav className="w-full">
            <Navbar toggle={toggleCart} navigation={toggleLinks} cantidad={cantidad}></Navbar>
          </nav>
          <div className="relative">
            <div className="absolute top-4 right-0 z-50 sm:w-[400px] w-full">
              <ul className="w-full flex flex-col gap-2">
               {messages.length > 0? messages.map((message, index) => (
               <Message key={index} text={"Se agrego: " + message.text}/>
               )):null} 
              </ul>
              
            </div>
          </div>
        </header>

        <main className="h-auto w-full block">
          <div className="w-full h-full">
            <Outlet/>
          </div>
        </main>
        
        <footer className="min-h-[100px] w-full block">
          <Footer/>
        </footer>

        <div className="sticky z-30 bottom-0 right-0 min-h-[50px] w-full flex items-center justify-center">
          <div className="w-full h-full flex justify-end">
            {/*<span>Bases y condiciones de la aplicacion</span>*/}
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
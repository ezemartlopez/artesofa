import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitleHash from "@components/TitleHash/TitleHash";
import PaymentMethods from "@components/PaymentMethods/PaymentMethods";
import Categories from "@components/Categories/Categories";
import InstagramLink from "@components/InstagramLink/InstagramLink";
import Slider from "@components/Slider/Slider";

function Home({addProduct}) {
  const url = "/";
  return (
    <>
        <Slider/>
        <ProductsContainer urlProducts={url} addProduct={addProduct}/>
        <TitleHash/>
        <Categories/>
        <PaymentMethods/>
        <InstagramLink/> 
    </>
  )
}

export default Home;
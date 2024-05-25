import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitleHash from "@components/TitleHash/TitleHash";
import PaymentMethods from "@components/PaymentMethods/PaymentMethods";
import Categories from "@components/Categories/Categories";
import InstagramLink from "@components/InstagramLink/InstagramLink";
import Slider from "@components/Slider/Slider";

function Home() {
  const url = "http://localhost:5000/";
  return (
    <>
        <Slider/>
        <ProductsContainer urlProducts={url}/>
        <TitleHash/>
        <Categories/>
        <PaymentMethods/>
        <InstagramLink/> 
    </>
  )
}

export default Home;
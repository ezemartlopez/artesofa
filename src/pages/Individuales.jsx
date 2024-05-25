import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Individuales() {
  const url = "http://localhost:5000/individuales/";
  return (
    <>
      <TitlePage titulo={"Individuales"} links={["", ">", "Individuales"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default Individuales;
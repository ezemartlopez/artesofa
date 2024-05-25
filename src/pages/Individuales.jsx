import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Individuales({addProduct}) {
  const url = "http://localhost:5000/individuales/";
  return (
    <>
      <TitlePage titulo={"Individuales"} links={["", ">", "Individuales"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Individuales;
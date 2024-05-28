import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Esquineros({addProduct}) {
  const url = "/esquineros/";
  return (
    <>
      <TitlePage titulo={"Esquineros"} links={["", ">", "Esquineros"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Esquineros;
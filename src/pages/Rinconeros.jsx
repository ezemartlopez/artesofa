import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Rinconeros({addProduct}) {
  const url = "/rinconeros/";
  return (
    <>
      <TitlePage titulo={"Rinconeros"} links={["", ">", "Rinconeros"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Rinconeros;
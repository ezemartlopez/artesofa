import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Muebles({addProduct}) {
  const url = "/muebles/";
  return (
    <>
      <TitlePage titulo={"Muebles"} links={["", ">", "Muebles"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Muebles;
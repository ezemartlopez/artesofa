import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Complemento({addProduct}) {
  const url = "/complemento/";
  return (
    <>
      <TitlePage titulo={"Complemento"} links={["", ">", "Complemento"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Complemento;
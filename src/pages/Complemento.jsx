import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Complemento({addProduct}) {
  const url = "http://localhost:5000/complemento/";
  return (
    <>
      <TitlePage titulo={"Complemento"} links={["", ">", "Complemento"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Complemento;
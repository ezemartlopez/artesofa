import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Complemento() {
  const url = "http://localhost:5000/complemento/";
  return (
    <>
      <TitlePage titulo={"Complemento"} links={["", ">", "Complemento"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default Complemento;
import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Esquineros() {
  const url = "http://localhost:5000/esquineros/";
  return (
    <>
      <TitlePage titulo={"Esquineros"} links={["", ">", "Esquineros"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default Esquineros;
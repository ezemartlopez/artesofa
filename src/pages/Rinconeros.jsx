import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Rinconeros() {
  const url = "http://localhost:5000/rinconeros/";
  return (
    <>
      <TitlePage titulo={"Rinconeros"} links={["", ">", "Rinconeros"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default Rinconeros;
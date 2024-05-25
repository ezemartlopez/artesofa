import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Rinconeros({addProduct}) {
  const url = "http://localhost:5000/rinconeros/";
  return (
    <>
      <TitlePage titulo={"Rinconeros"} links={["", ">", "Rinconeros"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Rinconeros;
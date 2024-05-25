import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Muebles({addProduct}) {
  const url = "http://localhost:5000/muebles/";
  return (
    <>
      <TitlePage titulo={"Muebles"} links={["", ">", "Muebles"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default Muebles;
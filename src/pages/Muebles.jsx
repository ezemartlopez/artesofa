import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Muebles() {
  const url = "http://localhost:5000/muebles/";
  return (
    <>
      <TitlePage titulo={"Muebles"} links={["", ">", "Muebles"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default Muebles;
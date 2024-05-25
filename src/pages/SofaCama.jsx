import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function SofaCama() {
  const url = "http://localhost:5000/sofas-cama/";
  return (
    <>
      <TitlePage titulo={"Sofás Cama"} links={["", ">", "Sofa Cama"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}


export default SofaCama;
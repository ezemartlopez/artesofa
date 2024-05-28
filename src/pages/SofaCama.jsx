import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function SofaCama({addProduct}) {
  const url = "/sofas-cama/";
  return (
    <>
      <TitlePage titulo={"Sofás Cama"} links={["", ">", "Sofa Cama"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default SofaCama;
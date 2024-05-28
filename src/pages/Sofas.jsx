import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Sofas({addProduct}) {
  const url = "/sofas/";
  return (
    <>
      <TitlePage titulo={"Sofás"} links={["", ">", "Sofas"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}

export default Sofas;
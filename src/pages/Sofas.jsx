import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function Sofas() {
  const url = "http://localhost:5000/sofas/";
  return (
    <>
      <TitlePage titulo={"Sofás"} links={["", ">", "Sofas"]}/>
      <ProductsContainer urlProducts={url}/>
    </>
  )
}

export default Sofas;
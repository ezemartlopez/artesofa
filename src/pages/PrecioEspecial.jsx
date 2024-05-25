
import ProductsContainer from "@components/ProductsContainer/ProductsContainer";
import TitlePage from "@components/titlePage/TitlePage";

function PrecioEspecial({addProduct}) {
  const url = "http://localhost:5000/precio-especial/";
  return (
    <>
      <TitlePage titulo={"Precio Especial"} links={["", ">", "Precio Especial"]}/>
      <ProductsContainer urlProducts={url} addProduct={addProduct}/>
    </>
  )
}


export default PrecioEspecial;
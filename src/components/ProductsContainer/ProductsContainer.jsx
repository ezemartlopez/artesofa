import CardProduct from "@components/CardProduct/CardProduct";
import useProducts from "./useProducts";

function ProductsContainer({urlProducts, addProduct}) {
  const customStyles = { gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', };
  const products = useProducts(urlProducts);
  //console.log("url: " + urlProducts);
  return (
    <div className="pt-4">
      <div className="w-auto grid gap-6" style={customStyles}>
        {products.map((product, index) => (<CardProduct key={index} product={product} addProduct={addProduct}/>))}
      </div>
    </div>

  );
}

export default ProductsContainer;
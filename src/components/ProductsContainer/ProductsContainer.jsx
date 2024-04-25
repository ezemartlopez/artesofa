import CardProduct from "@components/CardProduct/CardProduct";
import useProducts from "./useProducts";

function ProductsContainer() {
  const customStyles = { gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', };
  const products = useProducts();
  return (
    <div className="pt-4">
      <div className="w-auto grid gap-6" style={customStyles}>
        {products.map((product, index) => (<CardProduct key={index} product={product}/>))}
      </div>
    </div>

  );
}

export default ProductsContainer;
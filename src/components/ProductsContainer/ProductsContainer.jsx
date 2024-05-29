import CardProduct from "@components/CardProduct/CardProduct";
import useProducts from "@hooks/useProducts";
import './productsContainer.css';

function ProductsContainer({urlProducts, addProduct}) {
  //const customStyles = { gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', };
  const products = useProducts(urlProducts);
  //console.log("url: " + urlProducts);
  return (
    <div className="pt-4">
      <div className="w-full product-grid">
        {products.map((product, index) => (<CardProduct key={index} product={product} addProduct={addProduct}/>))}
      </div>
    </div>

  );
}

export default ProductsContainer;
import { useEffect, useState } from 'react';
const url = "http://localhost:3000/products";

function customProduct(product){
  let newData = {
    name: product.name,
    price: product.price,
    cash_price: product.cash_price,
    image: product.image_primary,
    image_hover: product.image_secondary
  };
  return newData;
}

function useProducts() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // Aquí obtienes los datos de respuesta como un objeto JSON
      let customData = data.map(customProduct);
      setProducts(customData); 
    })
    .catch(error => {
      console.error('There was a problem with your fetch operation:', error);
      setProducts([]);
    });
  }, []);
  return products;
}

export default useProducts
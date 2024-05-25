import { useEffect, useState } from 'react'
const CART_STORAGE_NAME = "cart_list";
function useCartShop() {
    const chargeCartShop = () =>{
        const storedListString = localStorage.getItem(CART_STORAGE_NAME);
        const currentList = JSON.parse(storedListString) || [];
        return currentList;
    }
    const createProdutcCart = (id, name, url_image, price) =>{
        let count = 1;
        return {id, name, url_image, price, count};
    }
    const [cartList, setCartList] = useState(chargeCartShop());

    const handleAddStorageCartList = (id, name, url_image, price) => {
        const existingProduct = cartList.find((product) => product.id === id);
      
        if (existingProduct) {
          setCartList((prevList) =>
            prevList.map((product) =>
              product.id === id
                ? { ...product, count: product.count + 1 }
                : product
            )
          );
        } else {
          const newProduct = createProdutcCart(id, name, url_image, price);
          setCartList((prevList) => [...prevList, newProduct]);
        }
    };

    useEffect(() => {
        //cargando info en la storage
        localStorage.setItem(CART_STORAGE_NAME, JSON.stringify(cartList));
    }, [cartList])
    return {cartList, addProduct: handleAddStorageCartList, amountProducts: cartList.length};
}

export default useCartShop;
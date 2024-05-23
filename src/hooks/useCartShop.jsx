import { useEffect, useState } from 'react'
const CART_STORAGE_NAME = "cart_list";
function useCartShop() {
    const chargeCartShop = () =>{
        const storedListString = localStorage.getItem(CART_STORAGE_NAME);
        const currentList = JSON.parse(storedListString) || [];
        return currentList;
    }
    const createProdutcCart = (id, name, url_image, price) =>{
        return {id, name, url_image, price};
    }
    const [cartList, setCartList] = useState(chargeCartShop());
    const handleAddStorageCartList = (id, name, url_image, price) =>{
        const producto = createProdutcCart(id, name, url_image, price);
        setCartList((lista) => [...lista, producto]);
    }

    useEffect(() => {
        //cargando info en la storage
        localStorage.setItem(CART_STORAGE_NAME, JSON.stringify(cartList));
    }, [cartList])
    return {cartList, addProduct: handleAddStorageCartList};
}

export default useCartShop;
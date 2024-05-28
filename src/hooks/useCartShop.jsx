import { useEffect, useState } from 'react';

const CART_STORAGE_NAME = "cart_list";

function useCartShop() {
    const chargeCartShop = () => {
        const storedListString = localStorage.getItem(CART_STORAGE_NAME);
        const currentList = JSON.parse(storedListString) || [];
        return currentList;
    };

    const createProductCart = (id, name, url_image, price) => {
        let count = 1;
        return { id, name, url_image, price, count };
    };

    const [cartList, setCartList] = useState(chargeCartShop());
    const [messages, setMessages] = useState([]);
    
    const addMessage = (message) =>{
        setMessages((prevList) => [...prevList, message]);
        const {id} = message;
        //console.log("Se agrego: " + message);
        deleteMessage(id);
    }
    const deleteMessage = (id) =>{
        setTimeout(() => {
            setMessages((messages) => messages.filter((message) => message.id !== id));
            //console.log("Se elimino: " + id);
            //console.log(messages);
        }, 5000);
    }
    const amountProducts = () => {
        return cartList.reduce((accumulator, item) => accumulator + item.count, 0);
    };

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
          const newProduct = createProductCart(id, name, url_image, price);
          setCartList((prevList) => [...prevList, newProduct]);
        }
        addMessage({id, text:name});
    };

    const removeProductById = (id) => {
        setCartList((prevList) => prevList.filter((product) => product.id !== id));
    };

    const incrementProductCount = (id) => {
        setCartList((prevList) =>
            prevList.map((product) =>
                product.id === id
                    ? { ...product, count: product.count + 1 }
                    : product
            )
        );
    };

    const decrementProductCount = (id) => {
        setCartList((prevList) =>
            prevList.map((product) =>
                product.id === id
                    ? { ...product, count: Math.max(product.count - 1, 1) }
                    : product
            )
        );
    };

    useEffect(() => {
        // Guardar información en localStorage
        localStorage.setItem(CART_STORAGE_NAME, JSON.stringify(cartList));
    }, [cartList]);

    return {
        cartList,
        addProduct: handleAddStorageCartList,
        amountProducts,
        removeProductById,
        incrementProductCount,
        decrementProductCount,
        messages
    };
}

export default useCartShop;

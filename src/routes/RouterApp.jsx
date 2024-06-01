import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Base from '../pages/Base';
import Home from '../pages/Home';
import Sofas from '../pages/Sofas';
import SofaCama from '../pages/SofaCama';
import Rinconeros from '../pages/Rinconeros';
import PrecioEspecial from '../pages/PrecioEspecial';
import Muebles from '../pages/Muebles';
import Individuales from '../pages/Individuales';
import Esquineros from '../pages/Esquineros';
import Complemento from '../pages/Complemento';
import useCartShop from "@hooks/useCartShop";
import Producto from '../pages/Producto';
function RouterApp() {
  const {cartList, addProduct, amountProducts, removeProductById, incrementProductCount, decrementProductCount, messages} = useCartShop();
  const cantidad = amountProducts();

  return (
    <Router>  
      <Routes>
        <Route path="/" element={<Base cantidad={cantidad} products={cartList} removeProductById={removeProductById} incrementProductCount={incrementProductCount} decrementProductCount={decrementProductCount} messages={messages}/>}>
          <Route path="" element={<Home addProduct={addProduct}/>} />
          <Route path="producto/:id" element={<Producto/>} />
          <Route path="sofas/" element={<Sofas addProduct={addProduct}/>} />
          <Route path="sofas-cama/" element={<SofaCama addProduct={addProduct}/>} />
          <Route path="rinconeros/" element={<Rinconeros addProduct={addProduct}/>} />
          <Route path="precio-especial/" element={<PrecioEspecial addProduct={addProduct}/>} />
          <Route path="muebles/" element={<Muebles addProduct={addProduct}/>} />
          <Route path="individuales/" element={<Individuales addProduct={addProduct}/>} />
          <Route path="esquineros/" element={<Esquineros addProduct={addProduct}/>} />
          <Route path="complemento/" element={<Complemento addProduct={addProduct}/>} />
        </Route>
      </Routes>
  </Router>
  )
}

export default RouterApp;
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

function RouterApp() {
  return (
    <Router>  
      <Routes>
        <Route path="/" element={<Base/>}>
          <Route path="" element={<Home />} />
          <Route path="sofas/" element={<Sofas/>} />
          <Route path="sofas-cama/" element={<SofaCama/>} />
          <Route path="rinconeros/" element={<Rinconeros/>} />
          <Route path="precio-especial/" element={<PrecioEspecial/>} />
          <Route path="muebles/" element={<Muebles/>} />
          <Route path="individuales/" element={<Individuales/>} />
          <Route path="esquineros/" element={<Esquineros/>} />
          <Route path="complemento/" element={<Complemento/>} />
        </Route>
      </Routes>
  </Router>
  )
}

export default RouterApp;
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';


function RouterApp() {
  return (
    <Router>  
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/dashboard/*" element={<Dashboard />} />
      </Routes>
  </Router>
  )
}

export default RouterApp;
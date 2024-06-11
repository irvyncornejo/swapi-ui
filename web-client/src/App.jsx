import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from './pages/Login'
import Home from './pages/Home'
import './App.css'

function App() {

  return (
      <BrowserRouter>
        <Routes>
          <Route path='' element={<Login />} />
          <Route path='/demo' element={<Home />} />
        </Routes>
      </BrowserRouter>
  )
}

export default App

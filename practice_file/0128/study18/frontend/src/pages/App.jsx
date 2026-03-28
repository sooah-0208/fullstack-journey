import { useState } from 'react'
import { AuthContext } from '@hooks/AuthContext.js'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import { BrowserRouter, Routes, Route } from "react-router";
import '@styles/App.css'
import Home from '@pages/Home.jsx'
import NotFound from '@pages/NotFound.jsx'
import Nav from '@pages/Nav.jsx'
import Login from '@pages/Login.jsx'

const App = () => {
  const [isLogin, setIsLogin] = useState(false)
  const paths = [
    {path: "/", element: <Home />},
    {path: "/login", element: <Login />},
    {path: "*", element: <NotFound />},
  ]
  return (
    <AuthContext.Provider value={{ isLogin, setIsLogin }}> 
    {/* 이 벨류가 전역변수 */}
      <Nav />
      <BrowserRouter>
        <Routes>
          { paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />) }
        </Routes>
      </BrowserRouter>
    </AuthContext.Provider> //전역변수 허용할 범위, 안 쓸 애들은 이 밖으로 빼주면 됨
  )
}

export default App
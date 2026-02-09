import { BrowserRouter, Routes, Route } from "react-router";
import AuthProvider from '@hooks/AuthProvider.jsx'
import { CookiesProvider } from 'react-cookie'
import Login from "./pages/Login";
import Home from "./pages/Home";
import Bag from "./pages/Bag";


const App = () => {
  const paths = [
    { path: "/", element: <Home /> },
    { path: "/login", element: <Login /> },
    { path: "/bag", element: <Bag /> },
  ]
  return (
    <>
      <CookiesProvider defaultSetOptions={{ path: '/' }}>
        <BrowserRouter>
          <AuthProvider>
            <Routes>
              {paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />)}
            </Routes>
          </AuthProvider>
        </BrowserRouter>
      </CookiesProvider>
    </>
  )
}

export default App
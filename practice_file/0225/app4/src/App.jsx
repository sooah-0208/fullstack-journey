
import './App.css'
import { Routes, Route } from "react-router"
import NotFound from './NotFound.jsx'
import Home from './home.jsx'



const paths = [
  { path: "/", element: <Home /> },
  { path: "*", element: <NotFound /> },
]


function App() {


  return (
    <>

      <Routes>
        {paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />)}
      </Routes>
    </>

  )
}

export default App


import '@/styles/App.css'
import { Routes, Route } from "react-router"
import NotFound from '@pages/NotFound.jsx'
import Home from '@pages/home.jsx'



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

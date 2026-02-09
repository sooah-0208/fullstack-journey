import { Routes, Route, BrowserRouter } from "react-router"

const NotFound = () => {
  return (
    <div>
      <h1>404</h1>
      <p>페이지를 찾을 수 없습니다.</p>
    </div>
  )
}

const Home = ()=>{
  return(
    <h1>메인화면</h1>
  )
}

function App() {
   const paths = [
    {path: "/", element: <Home />},
    {path: "*", element: <NotFound />},
  ]
  return (
    <BrowserRouter>
      <Routes>
        { paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />) }
      </Routes>
    </BrowserRouter>
  )
}

export default App

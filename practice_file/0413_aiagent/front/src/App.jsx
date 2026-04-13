import Board from './pages/board'
import './App.css'
import { Route, Routes } from 'react-router'


function App() {
  const paths = [
  { path: "/", element: <Board /> },
  // { path: "*", element: <NotFound /> },
]

  return (
     <>
      <Routes>
        {paths.map((v, i) => <Route key={i} path={v.path} element={v.element} />)}
      </Routes>
    </>
  )
}

export default App

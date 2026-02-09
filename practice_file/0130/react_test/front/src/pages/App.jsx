import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import Home from './Home'
import Login from './user/Login'
import SingUp from './user/SingUp'
import UserEdit from './user/UserEdit'
import UserView from './user/UserView'
import BoardAdd from './board/BoardAdd'
import BoardEdit from './board/BoardEdit'
import BoardView from './board/BoardView'

function App() {

  const routes = [
    {path:'/', element:<Home/>},
    {path:'/login', element:<Login />},
    {path:'/singup', element:<SingUp />},
    {path:'/useredit', element:<UserEdit />},
    {path:'/userview', element:<UserView />},
    {path:'/boardadd', element:<BoardAdd />},
    {path:'/boardedit', element:<BoardEdit />},
    {path:'/boardview', element:<BoardView />},
  ]
  return (
     <BrowserRouter>
     <Nav/>
      <Routes>
        {
          routes?.map(v => (
            <Route path={v.path} element={v.element} />
          ))
        }
      </Routes>
    
    </BrowserRouter>
  )
}

export default App

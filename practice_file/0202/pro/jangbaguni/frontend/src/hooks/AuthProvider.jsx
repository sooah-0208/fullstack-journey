import { createContext, useContext, useState, useEffect } from "react"
import { useNavigate } from "react-router";
import { api } from '@utils/network.js'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {


  const [isLogin, setIsLogin] = useState(false)
  const [bags, setBags] = useState([])
  const navigate = useNavigate()

  const setAuth = status => {
    localStorage.setItem("user", status)
    setIsLogin(status)
    navigate("/")
  }

  const clearAuth = () => {
    api.post("/logout")
    localStorage.removeItem("user")
    setIsLogin(false)
    navigate("/")
  }

  const removeAuth = () => {
    clearAuth()
  }

  const checkAuth = () => {
    return localStorage.getItem("user") ? true : false
  }

  const addBagAuth = ()=>{
    api.get('/bag')
    .then(res=>{
      if(res.data.bags){
        setBags(...bags, data)
      }
    })
  }

  // const userAuth =  ()=>{
  //   if(cookieStore.getItem('token') == token['id']){
  //     setBags('token'.id)
  //   }
  // }

  useEffect(() => {
    api.get('/me')
    .then(res=>{
      if(res.data.status){
        setIsLogin(true)
      }else setIsLogin(false)
    })

  }, [])

  return (
    <AuthContext.Provider value={{ bags,isLogin, setAuth, removeAuth, clearAuth, checkAuth }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)

export default AuthProvider
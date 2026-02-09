import { createContext, useContext, useState, useEffect } from "react"
import { useNavigate } from "react-router";
import { api } from '@utils/network.js'

export const AuthContext = createContext()

const AuthProvider = ({ children }) => {
  const [isLogin, setIsLogin] = useState(false)
  const navigate = useNavigate()
  const setAuth = (status) => {
    localStorage.setItem("user", status)
    setIsLogin(status)
  }

  const clearAuth = () => {
    api.post("/logout")
      .then(res => {
        if (res.data.status) {
          alert(res.data.msg)
          setIsLogin(false)
          navigate("/")
        }
      })
  }

  const removeAuth = () => {
    clearAuth(false)
  }

  const checkAuth = () => {
      try {
      const res =  api.get("/me")
      if (res.data?.status) {
        setIsLogin(true)
        return true
      }
    } catch (err) {
      setIsLogin(false)
      return false
    }
  }
  

  useEffect(() => {

  }, [])


  return (
    <AuthContext.Provider value={{ isLogin, setAuth, removeAuth, clearAuth, checkAuth }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)

export default AuthProvider
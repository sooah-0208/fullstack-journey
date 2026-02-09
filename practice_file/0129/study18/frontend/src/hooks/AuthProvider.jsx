import { createContext, useContext, useState, useEffect } from "react"
import { useNavigate } from "react-router";
import axios from "axios"  //백 과 프론트 연결

const api = axios.create({          //axios기본 설정을 api에 담아둠, 매 함수마다 치기 귀찮으니까
  baseURL: "http://localhost:8000", 
  withCredentials: true,            //main.py에서 크러덴셜즈 허용했으니 여기도 쿠키 허용해줘야 넘길 수 있음
  headers: {
    "Content-Type": "application/json",
  },
})

export const AuthContext = createContext()

const AuthProvider = ({children}) => {
  const [isLogin, setIsLogin] = useState(false)
  const navigate = useNavigate()

  const setAuth = status => {             // status를 인자로 받음
    localStorage.setItem("user", status)  // 로컬스토리지에 setItem저장
    setIsLogin(status)                    // 받아온 status로 로그인한지 안한지 상태 변경시킴
    navigate("/")                         //->실행은 Login.jsx에서
  }

  const removeAuth = () => {
    
    api.post("/logout")   // 로그아웃 버튼 누르면, 로그아웃 페이지 정보로 넘어가고
    .then(res => {
      console.log(res)
      localStorage.removeItem("user")  //스토리지에 있는 유저정보를 지움
      setIsLogin(false)                // 로그인했니? => 아니오로 바꿔줌
      navigate("/")                    // 이제 메인페이지로 꺼져
    })
    .catch(err => console.error(err))
    
  }

  useEffect(() => {
    if(localStorage.getItem("user")) setIsLogin(true)
  }, [])

  return (
    <AuthContext.Provider value={{ isLogin, setAuth, removeAuth }}>
      {/* 👆여기서 전역변수로 뿌림*/}
      {children}
      {/* children = App.jsx에 AuthProvider 안에 있는 애들, 걔네가 value를 받음 */}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)

export default AuthProvider
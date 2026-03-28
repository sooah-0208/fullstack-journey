// import { useAuth } from '@hooks/AuthProvider.jsx'
import axios from "axios"
import { useState } from 'react'
import {jwtDecode} from 'jwt-decode'


const api = axios.create({
  baseURL: "http://localhost:8000",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
})

const Login = () => {
  
  const [email,setEmail]= useState('')
  const [pwd, setPwd]= useState('')
  // const { setAuth } = useAuth()
  // const submitEvent = e => {
  //   e.preventDefault()

  //   const params = {
  //     "email": e.target.email.value,
  //     "pwd": e.target.pwd.value
  //   } 
  //   api.post("/login", params)  //지정 params에 대한 요청
  //   .then(res => {              //.then: 성공시 핸들링
  //     console.log(res)
  //     setAuth(res.data.status)  //main.py에서 받아오는 정보
  //   })
  //   .catch(err => console.error(err))  //.catch 에러핸들링
  //                                     //.finally 항상 실행(에러 나든말든)
  // }
  // const checkEvent = () => {

  //   api.get("/user")               //axios baseURL뒤에 /user로 지정
  //   .then(res => console.log(res))
  //   .catch(err => console.error(err))

  // }

  const submitEvent = (e) => {
    e.preventDefault()
    const params = {
      email,pwd
    }
    api.post('/key', params)
    .then(res=>{
      console.log(res)
      if(res.data.status){
        console.log(res.data.access_token)
      }
    })
  }

  return (
    <>
    
    <div className="container mt-3">
			<h1 className="display-1 text-center">로그인</h1>
			<form onSubmit={submitEvent}>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요." value={email} onChange={e=>setEmail(e.target.value)} required={true} autoComplete="off" />
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." value={pwd} onChange={e=>setPwd(e.target.value)}required={true} autoComplete="off" />
				</div>
        <div className="d-flex">
          <div className="p-2 flex-fill d-grid">
            <button type="submit" className="btn btn-primary">로그인</button>
          </div>
          <div className="p-2 flex-fill d-grid">
            <button type="button" className="btn btn-primary" 
            // onClick={checkEvent}
            >취소</button>
          </div>
        </div>
			</form>
		</div>
    </>
  )
}

export default Login
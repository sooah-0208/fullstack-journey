import { useState } from "react"
import { useNavigate } from "react-router"
const Login = ()=>{
	const [email, setEmail]=useState('')
	const [pwd, setPwd]=useState('')
	const nav = useNavigate()
	
	const onsubmit=(e)=>{
		e.preventDefault()
	}
	
	const UserLogin = ()=>{
		nav('/',{state:{email, pwd}})
		localStorage.setItem('key',email)
	}
	const cancle = ()=>{
		setEmail('')
		setPwd('')
	}
    return(
        <>
        <div className="container mt-3">
			<h1 className="display-1 text-center">로그인</h1>
			<form onSubmit={onsubmit}>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요."  value={email}
					onChange={(e)=>(setEmail(e.target.value))}/>
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." value={pwd}
					onChange={(e)=>(setPwd(e.target.value))}/>
				</div>
			</form>
			<div className="d-flex">
				<div className="p-2 flex-fill d-grid">
					<button className="btn btn-primary" onClick={UserLogin}>로그인</button>
				</div>
				<div className="p-2 flex-fill d-grid">
					<button className="btn btn-primary" onClick={cancle}>취소</button>
				</div>
			</div>
		</div>
        </>
    )
}

export default Login
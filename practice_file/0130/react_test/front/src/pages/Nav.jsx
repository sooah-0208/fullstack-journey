import { useNavigate } from "react-router"
import { useState, useEffect } from "react"
const Nav = () => {
    const nav = useNavigate()
    const [state, setState] = useState(false)
    return(
        <>
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
			<div className="container-fluid">
				<button className="navbar-brand" onClick={()=>nav('/')}>수아짱짱맨뿡뿡</button>
				<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarNav">
					<ul className="navbar-nav">
						<li className="nav-item">
							<button className="nav-link" onClick={()=>{nav('/login'), setState(!state)}}>{state == false? '로그인': '로그아웃'}</button>
						</li>
						<li className="nav-item">
							<button className="nav-link" onClick={()=>nav("/singup")}>회원가입</button>
						</li>
						<li className="nav-item">
							<button className="nav-link" onClick={()=>nav("/userview")}>회원정보</button>
						</li>
					</ul>
				</div>
			</div>
		</nav>
        </>
    )
}

export default Nav
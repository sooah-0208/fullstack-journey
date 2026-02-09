import { useAuth } from '@hooks/AuthProvider.jsx'

const Nav = () => {
  const { isLogin, removeAuth } = useAuth()
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
			<div className="container-fluid">
				<a className="navbar-brand" href="/">TEAM3</a>
				<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarNav">
					<ul className="navbar-nav" me-auto="true">
            {
              !isLogin && 
              <>
              <li className="nav-item">
                <a className="nav-link" href="/login">로그인</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">회원가입</a>
              </li>
              </>
            }
            {
              isLogin && 
              <>
                <li className="nav-item">
                  <button className="nav-link" onClick={()=>removeAuth()}>로그아웃</button>  
                  {/* 로그아웃버튼을 누르면 removeAuth()실행 -> AuthProvider.jsx에 할당한 함수 실행 */}
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">회원정보</a>
                </li>
              </>
            }
						
					</ul>
				</div>
			</div>
		</nav>
  )
}

export default Nav
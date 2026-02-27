import { useEffect, useState } from "react"
import { api } from '/utils/network.js'
import { useNavigate } from 'react-router-dom'

const Home = () => {

    const [isLogin, setIsLogin] = useState(false)
    const [profile, setProfile] = useState(0)
    const [profilePath, setProfilePath] = useState(0)
    const nav = useNavigate()
    const path = import.meta.env.VITE_APP_FASTAPI_URL || "http://localhost:8001"

  const kakaoLogin = () => {
    // axios(api.get) 대신 브라우저 주소창을 직접 백엔드 로그인 경로로 이동시켜!
    window.location.href = 'http://aiedu.tplinkdns.com:6202/app1/login/kakao';
};

    const removeAuth = () => {
        api.get("/logout")
            .then(res => {
                if (res.data.status) {
                    setIsLogin(false)
                    nav("/")
                }
            })
            .catch(err => console.error(err))
    }

    // 로그인 시 프로필 사진 반영
    // useEffect(() => {
    // 	if (isLogin) {
    // 		api.post("/me")
    // 			.then(res => {
    // 				setChangeProfile(res.data.user.profileNo)
    // 			})
    // 	}
    // }, [isLogin])

	const [name, setName] = useState('')

	// 초기값 불러오기
	useEffect(() => {
        
		// api.get("/me")
		// 	.then(res => {
		// 		setName(res.data.userInfo.nickname)
		// 		setProfile(res.data.userInfo.profile_image)
		// 	})
	}, [])



    return (
        <>
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
                <div className="container-fluid position-relative">
                    <a className="navbar-brand" style={{ "cursor": "pointer" }} onClick={() => nav("/")}>TEAM2</a>
                    <div className="d-flex">
                        {
                            isLogin && <img src={profile} className="border user_pt_nav01 mt-1 object-fit-cover" onClick={() => nav('/userview')} />
                        }
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                    </div>
                    <div className="collapse navbar-collapse w-100" id="navbarNav">
                        <div className="nav_box">
                            <ul className="navbar-nav mt-2 me-auto">
                                {
                                    !isLogin &&
                                    <>
                                        <li className="nav-item">
                                            {/* <button type="button" className="nav-link" onClick={() => kakaoLogin()}>로그인</button> */}
                                            <a href="http://aiedu.tplinkdns.com:6202/app1/login/kakao" className="nav-link" >로그인</a>
                                        </li>
                                        <li className="nav-item">
                                            <button type="button" className="nav-link" onClick={() => kakaoLogin()}>회원가입</button>
                                        </li>
                                    </>
                                }
                                {
                                    isLogin &&
                                    <>
                                        <li className="nav-item">
                                            <button type="button" className="nav-link" onClick={() => removeAuth()} >로그아웃</button>
                                        </li>
                                        <li className="nav-item">
                                            <button type="button" className="nav-link" onClick={() => nav("/")}>회원정보</button>
                                        </li>
                                    </>
                                }
                            </ul>
                            {
                                isLogin && <img src={profile} className="border user_pt_nav mt-1 object-fit-cover" onClick={() => nav('/')} />
                            }
                        </div>
                    </div>
                </div>
            </nav>
            <div className="container mt-3 position-relative">
			<h1 className="display-1 text-center">회원정보</h1>
			<div>
				<img src={profile} className="border user_pt_view" />
			</div>
			<form>
				<div>
					<div className="mb-3 mt-3">
						<label htmlFor="name" className="form-label">이름</label>
						<input type="text" className="form-control" id="name" name="name" readOnly="readonly" defaultValue={name} />
					</div>
				</div>
				<div className="d-flex">
					<div className="p-2 flex-fill d-grid">
						<button type="button" onClick={() => nav("/")} className="btn btn-primary">취소</button>
					</div>
					<div className="p-2 flex-fill d-grid">
						<button type="button" onClick={() => nav("/useredit")} className="btn btn-primary">수정</button>
					</div>
					<div className="p-2 flex-fill d-grid">
						<button type="button" onClick={() => delYn()} className="btn btn-primary">탈퇴</button>
					</div>
				</div>
			</form>
		</div>
        </>
    )
}


export default Home
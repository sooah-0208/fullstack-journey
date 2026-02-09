import { useNavigate } from "react-router";
import { useEffect, useState } from "react";
import { useAuth } from "../hooks/AuthProvider";
import { useCookies } from 'react-cookie';
import { productArr } from "../data/data";

const Home = () => {

    const [selected, setSelected] = useState([])
    const { isLogin, checkAuth, clearAuth } = useAuth()

    const nav = useNavigate()

    const [cookies, setCookie, removeCookie] = useCookies(['jangbaguni']);

    const check = (v) => {
        if (selected.includes(v)) {
            setSelected(selected.filter(v => v !== v))
        } else {
            setSelected([...selected, v])
        }
    }
    const submitEvent = (e) => {
        e.preventDefault()
        if (checkAuth()) {nav('/bag')
        setCookie('jangbaguni', JSON.stringify(selected), { path: '/', maxAge: 24 * 60 * 60 })}
        else alert('로그인이 필요합니다.')
        console.log(selected)
    }

    const alert_login = ()=>{
         if (checkAuth()) {nav('/bag')}
        // setCookie('jangbaguni', JSON.stringify(selected), { path: '/', maxAge: 24 * 60 * 60 })}
        else alert('로그인이 필요합니다.')
    }


    return (
        <>
            {/* NAVBAR */}
            <nav className="navbar navbar-expand-md bg-dark sticky-top border-bottom" data-bs-theme="dark">
                <div className="container">
                    <a className="navbar-brand d-md-none" href="#">Aperture</a>

                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvas"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="offcanvas offcanvas-end" id="offcanvas">
                        <div className="offcanvas-header">
                            <h5 className="offcanvas-title">Aperture</h5>
                            <button className="btn-close" data-bs-dismiss="offcanvas"></button>
                        </div>

                        <div className="offcanvas-body">
                            <ul className="navbar-nav flex-grow-1 justify-content-between">
                                <li className="nav-item"><button className="nav-link" onClick={() => {if(isLogin) {clearAuth()} else nav('/login')}}>{isLogin ? 'Logout' : 'Login'}</button></li>
                                <li className="nav-item"><a className="nav-link" href="#">Product</a></li>
                                <li className="nav-item"><a className="nav-link" href="#">Features</a></li>
                                <li className="nav-item"><button className="nav-link" onClick={alert_login}>장바구니</button></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>

            {/* HERO */}
            <main>
                <div className="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-body-tertiary">
                    <div className="col-md-6 p-lg-5 mx-auto my-5">
                        <h1 className="display-3 fw-bold">Designed for engineers</h1>
                        <h3 className="fw-normal text-muted mb-3">
                            Build anything you want with Aperture
                        </h3>
                        <div className="d-flex gap-3 justify-content-center lead fw-normal">
                            <a className="icon-link" href="#">Learn more</a>
                            <a className="icon-link" href="#">Buy</a>
                        </div>
                    </div>
                </div>

                {/* SECTIONS */}
                <form onSubmit={submitEvent}
                    className="d-md-flex flex-md-equal w-100 my-md-3 ps-md-3">
                    <button type="submit">담기</button>
                    {
                        productArr?.map((v, i) => (
                            <div key={i}
                                className="text-bg-dark me-md-3 pt-3 px-3 text-center overflow-hidden"
                            >
                                <div className="my-3 py-3">
                                    <input type="checkbox" name="product" id={v.no} value={v.title}
                                        onChange={() => { check(v) }} />
                                    <h2 className="display-5">{v.title}</h2>
                                    <p className="lead">And an even wittier subheading.</p>
                                </div>
                                <div className="bg-body-tertiary shadow-sm mx-auto"
                                    style={{ width: '80%', height: '300px', borderRadius: '21px 21px 0 0' }}>
                                </div>
                            </div>
                        ))
                    }
                </form>
            </main>

            {/* FOOTER */}
            <footer className="container py-5">
                <div className="row">
                    <div className="col-12 col-md">
                        <small className="d-block mb-3 text-body-secondary">
                            © 2017–2025
                        </small>
                    </div>
                </div>
            </footer>
        </>
    )
}

export default Home
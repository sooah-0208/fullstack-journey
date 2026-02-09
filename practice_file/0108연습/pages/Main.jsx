import { useNavigate, useParams} from "react-router"
import { list } from "../../data.js"

const Main = () => {
    const navigate = useNavigate()

    return (
        <div className="container mt-3">
            <h1 className="text-center bg-success text-dark bg-opacity-50">MAIN</h1>
            <div className="btn-group">
                <button onClick={() => navigate("/signIn")} type="button" className="btn btn-warning" >SignIn</button>
                <button onClick={() => navigate("/signUp")} type="button" className="btn btn-primary">SignUp</button>
            </div>
            <div className="row mt-2">
                <div className="col-12 col-md-6 col-lg-4 mb-3">
                    <div className="row mt-2">
                        {
                            list?.map((v,i) => (
                                <div key={v.id} className="col-12 col-md-6 col-lg-4 mb-3">
                                    <div className="card">
                                        <img className="card-img-top" src={v.img} alt="Card image" />
                                        <div className="card-body">
                                            <h4 className="card-title">{v.name}</h4>
                                            <p className="card-text">{v.job}</p>
                                            <button onClick={() => navigate(`/user/${i}`)} className="btn btn-primary">See Profile</button>
                                        </div>
                                    </div>
                                </div>
                            ))
                        }

                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main
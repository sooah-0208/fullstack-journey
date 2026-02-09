import { useNavigate } from "react-router"
import { useState } from "react"
import { list } from "../../data.js"


const SignIn = () => {
   const navigate = useNavigate()
   const close = () => navigate('/')
    const [data,setData] = useState({
    email: "",
    pwd: "",
  })
   const onSubmit = (e) => {     
    e.preventDefault()
    const correct = list.filter( v => v.email === data.email)
    console.log(correct)

    
    

    // if(setData === data) return 
    // const data = {email, password}
    // console.log(data)
    // navigate("/user", {state})
  }

  return (
    <div className="container mt-3">
    <h1 className="text-center bg-success text-dark bg-opacity-50">SignIn</h1>
    <form onSubmit={onSubmit}>
      <div className="mb-3 mt-3">
        <label htmlFor="email">Email:</label>
        <input type="email" className="form-control" id="email" placeholder="Enter email" name="email" value={data.email} required onChange={(e)=>setData({...data, email : e.target.value})} />
      </div>
      <div className="mb-3">
        <label htmlFor="pwd">Password:</label>
        <input type="password" className="form-control" id="pwd" placeholder="Enter password" name="pwd" value={data.pwd} required onChange={(e)=>setData({...data, pwd: e.target.value})} />
      </div>
      <div className="d-flex">
        <div className="p-2 flex-fill d-grid">
          <button type="submit" className="btn btn-warning">SignIn</button>
        </div>
        <div className="p-2 flex-fill d-grid">
          <button type="button" onClick={()=>navigate("/signUp")} className="btn btn-primary">SignUp</button>
        </div>
        <div className="p-2 flex-fill d-grid">
          <button type="button" onClick={close} className="btn btn-danger">Cancel</button>
        </div>
      </div>
    </form>
  </div>
  )
}

export default SignIn
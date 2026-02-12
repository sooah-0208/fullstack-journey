import { useState } from 'react'
import axios from "axios"

const App = () => {
  const [token, setToken] = useState("")
  const [no, setNo] = useState("")
  const [name, setName] = useState("")
  const [algorithm, setAlgorithm] = useState("")
  const [type, setType] = useState("")
  
  const reset = () => {
    setToken("")
    setNo("")
    setName("")
    setAlgorithm("")
    setType("")
  }

  const event1 = e => {
    e.preventDefault()
    console.log("코드 발급", e.target.email.value)
    axios.post("http://localhost:8001/login", {"email": e.target.email.value})
    .then(res => {
      console.log(res)
      if(res.data.status) {
        e.target.email.value = ""
        alert("Email 발급 되었습니다.")
      } else alert("입력하신 Email은 존재하지 않습니다.")
    })
    .catch(err => console.error(err))
  }
  

  const event2 = e => {
    e.preventDefault()
    console.log("토큰 발급", e.target.code.value)
    axios.post("http://localhost:8001/code", {"id": e.target.code.value})
    .then(res => {
      console.log(res)
      if(res.data.status) {
        setToken(res.data.access_token)
        alert("토큰 발급 되었습니다.")
      } else alert("입력하신 토큰은 존재하지 않습니다.")
      e.target.code.value = ""
    })
    .catch(err => console.error(err))
  }

  const event3 = e => {
    e.preventDefault()
    console.log("사용자 정보 요청")
    axios.post("http://localhost:8001/me", {}, 
      {headers: {"Authorization": `Bearer ${token}`}} // header로 보내는 방식
    ).then(res => {
      console.log(res)
      if(res.data.status) {
        
        // 체크 필요!!!
        // JWT Header 디코딩
        const headerBase64 = token.split(".")[0]
        const headerJson = JSON.parse(
          decodeURIComponent(
            atob(headerBase64)
            .split("")
            .map(c => "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2))
            .join("")
          )
        )
        // JWT Header 디코딩을 라이브러리를 사용하여 변경할 경우 아래 코드를 각 위치에 선언하여 사용
        // 실무 / 유지보수에 많이 사용
        // 1. npm install jwt-decode
        // 2. import jwtDecode from 'jwt-decode' 
        // 3. const header = jwtDecode(token, { header: true })

        // 만료 체크를 위해 선언
        // const now = Math.floor(Date.now() / 1000)
        // if (payload.exp && payload.exp < now) {
        //   alert("토큰이 만료되었습니다. 다시 코드 발급을 진행해주세요.")
        //   reset()
        //   return
        // }
        
        setAlgorithm(headerJson.alg)
        setType(headerJson.typ)

        setNo(res.data.no)
        setName(res.data.name)
        alert(`${res.data.name}님 안녕하세요.\n반갑습니다.`)
      } else alert("사용자를 불러오지 못하였습니다.")
    })
    .catch(err => console.error(err))
  }

  return (
    <div id="app">
      <main>
        <h1>Hello JWT!</h1>
        <div className="body">
          <hr />
          <h2>Token Code</h2>
          <form onSubmit={event1}>
            <div className="form-group">
              <input type="email" className="form-control" placeholder="이메일를 입력하세요." name="email" required />
            </div>
            <div className="form-group">
              <input type="submit" className="btn" value="생성" />
            </div>
          </form>
        </div>
        <div className="body">
          <hr />
          <h2>Token Authorize</h2>
          <form onSubmit={event2}>
            <div className="form-group">
              <input type="text" className="form-control" placeholder="코드를 입력하세요." name="code" required />
            </div>
            <div className="form-group">
              <input type="submit" className="btn" value="생성" />
            </div>
          </form>
        </div>
        <div className="body">
          <hr />
          <h2>Token Verification</h2>
          <div>
            <p>Token :</p>
            <textarea className="token" cols="30" rows="12" defaultValue={token}></textarea>
            <form onSubmit={event3}>
              <div className="form-group">
                <input type="hidden" className="form-control" placeholder="Token를 입력하세요." readOnly />
              </div>
              <div className="form-group">
                <input type="submit" className="btn" value="검증" />
              </div>
            </form>
          </div>
          <div>
            <div className="token-body">
              <h3>Header</h3>
              <p>Algorithm : <span className="token">{no ? algorithm : "algorithm"}</span></p>
              <p>Type : <span className="token">{no ? type : "Type"}</span></p>
            </div>
            <div className="token-body">
              <h3>Payload</h3>
              <p>No : <span className="token" >{no ? no : "no"}</span></p>
              <p>Name : <span className="token" >{no ? name : "name"}</span></p>
            </div>
            <div>
              <button className="btn" onClick={reset}>초기화</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App

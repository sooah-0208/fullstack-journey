import axios from "axios"
import { useState } from "react"


const App = () => {
  const [email, setEmail] = ('santacoyaki11@gmail.com')
  const [code, setCode] = ('')
  const [token, setToken] = ('')
  const event1 = e => {
    e.preventDefault()
    axios.get('http://t2s3.quadecologics.cloud:6202/login/kakao')
    .then(res=>{
      if(res){
      console.log(res)
      }
    })
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
              <input type="email" className="form-control" placeholder="이메일를 입력하세요." name="email" value={email} onChange={e=>setEmail(e.target.value)} required />
            </div>
            <div className="form-group">
              <input type="submit" className="btn" value="생성" />
            </div>
          </form>
        </div>
        <div className="body">
          <hr />
          <h2>Token Authorize</h2>
          <form>
            <div className="form-group">
              <input type="text" className="form-control" placeholder="코드를 입력하세요." name="code" value={code} onChange={e=>setCode(e.target.value)} required />
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
            <textarea className="token" cols="30" rows="12" defaultValue="token">{token}</textarea>
            <form>
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
              <p>Algorithm : <span className="token">algorithm</span></p>
              <p>Type : <span className="token">type</span></p>
            </div>
            <div className="token-body">
              <h3>Payload</h3>
              <p>No : <span className="token">no</span></p>
              <p>Name : <span className="token">name</span></p>
            </div>
            <div>
              <button className="btn">초기화</button>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App

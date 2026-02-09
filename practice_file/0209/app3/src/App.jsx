import { useState } from 'react'
import axios from 'axios';


function App() {
  const [token, setToken] = useState("")
  const api = axios.create({
    baseURL: "http://localhost:8001",
    withCredentials: true,
    headers: {
      "Content-Type": "application/json"
    }
  })
  const evnet1 = e => {
    e.preventDefault()
    console.log("코드발급: ", e.target.email.value)
    api.post('/login', { "email": e.target.email.value })
      .then(res => {
        console.log(res)
        if (res.data.status) {
          // e.target.email.value = ""
          alert("Email이 발송되었습니다.")
        }
        else alert("Email을 확인해주세요")
      })
      .catch(err => console.error(err))
  }
  const evnet2 = e => {
    e.preventDefault()
    console.log("토큰발급: ", e.target.code.value)
    api.post('/code', { "id": e.target.code.value })
      .then(res => {
        console.log(res.data.access_token)
        if (res.data.status) {
          // 여기 res에서 온 data는 back에서 api return값으로 보낸 정보들 중에 data임
          // e.target.code.value = ''
          setToken(res.data.access_token)
          alert('토큰이 발급되었습니다.')
        }
        else alert('인증번호를 확인해주세요')
      })
      .catch(err => console.error(err))

  }
  const evnet3 = e => {
    e.preventDefault()
    console.log("사용자 정보 요청", token)
    api.post('/me', {}, { headers: { "Authorization": `Bearer ${token}` } })
      .then(res => {
        console.log(res)
        if (res.data.status) {
          console.log(res.data.name)
        }
      })
      .catch(err => console.error(err))
  }

  return (
    <>
      <form onSubmit={evnet1}>
        <input type="email" name='email' required autoComplete='off' />
        <button type='sumbit'>코드 발급</button>
      </form>
      <hr />
      <form onSubmit={evnet2}>
        <input type="text" name='code' />
        <button type='sumbit'>토큰 발급</button>
      </form>
      <hr />
      <button type='button' onClick={evnet3}>사용자 정보</button>
    </>
  )
}

export default App

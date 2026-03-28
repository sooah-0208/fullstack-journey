import { useEffect, useState } from "react"
import axios from "axios"



function App() {
  const [email, setEmail] = useState("")
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")

  const submitEvent = e => {
    e.preventDefault()
    axios.post('http://127.0.0.1:8002/pd',
      { email,title, content })
      .then(res => console.log("성공", res))
      .catch(err => console.log("실패", err))
  }

  return (
    <>
      <div className="container mt-3">
        <h1 className="display-1 text-center">메일 작성</h1>
        <form onSubmit={submitEvent}>
          <div className="mb-3 mt-3">
            <label htmlFor="title" className="form-label">제목</label>
            <input type="text" className="form-control" id="title" placeholder="제목을 입력하세요." name="title" value={title}
              onChange={e => setTitle(e.target.value)} required={true} />
          </div>
          <div className="mb-3 mt-3">
            <label htmlFor="name" className="form-label">받으시오~!</label>
            <input type="email" className="form-control" id="name" placeholder="이메일을 입력하세요."
              value={email} required={true} onChange={e => setEmail(e.target.value)} />
          </div>
          <div className="mb-3 mt-3">
            <label htmlFor="content" className="form-label">내용</label>
            <textarea type="text" className="form-control h-50" rows="10" placeholder="내용을 입력하세요." name="content"
              value={content} onChange={e => setContent(e.target.value)} required={true}></textarea>
          </div>
          <div className="d-flex">
            <div className="p-2 flex-fill d-grid">
              <button type='submit' className="btn btn-primary">등록</button>
            </div>
            <div className="p-2 flex-fill d-grid">
              <button type='button' className="btn btn-primary">취소</button>
            </div>
          </div>
        </form>
      </div>
    </>
  )
}

export default App

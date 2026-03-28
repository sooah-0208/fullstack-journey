import axios from 'axios'

const Home = () => {
  const btn1Event = () => {
    console.log("btn1 호출")

    axios.get("http://localhost:8000/")
      .then(res => {
        console.log(res.data)
        // res 찍어보면 여러 객체로 와서 거기서 data만 꺼내는 것
        if(res.data.status) {
          alert(res.data.result[0])
        } else {
          alert("오류 발생")
        }
      })
      .catch(err => console.error(err))
      .finally(() => console.log("완료"))

  }
  return (
    <div className="text-center">
      <h1>메인 화면입니다.</h1>
      <button type="button" onClick={btn1Event}>FastAPI 확인</button>
    </div>
  )
}

export default Home
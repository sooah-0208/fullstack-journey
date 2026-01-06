export로 보내고 import로 받기
1. `import Update from "./Update.jsx"`
해당 페이지에 export default가 있음 => 얘는 딱 하나의 컴포넌트만 export할 수 있음
import로 받을 때 주소가 정확하다면 Update는 내 마음대로 이름 바꿔도 됨. 어차피 그 파일엔 실행시킬 컴포넌트가 하나니까.

2. `import { NotFound, Footer } from "./Not_Footer.jsx"`
해당 페이지에 export 컴포넌트가 여러개 있음
그 페이지의 원하는 컴포넌트를 {}안에 불러올 수 있음
여러개 중 원하는 걸 뽑아오니까 이름이 정확해야함

3. `import { BrowserRouter, Routes, Route } from "react-router";`
이처럼 페이지가 아니라 react, router, bootstrap 등의 기능을 받아오기도 함


map 함수 완벽 사용

배열명.map((받는 값)=>(재배열할 상태))

```
const menu = [
    {path: "/new", lable:"Create"},
    {path: "/detail", lable:"Detail"},
    {path: "/edit", lable:"Update"},
    {path: "/404", lable:"404"},
  ]

   {
    menu.map((v,i)=>(
    <li key={i} className="nav-item">
    <a className="nav-link" href={v.path}>{v.lable}</a>
    </li>
    ))
    }
```
(v,i)는 menu[0]의 값, [0]...<menu.length 임
key가 id라면 i는 굳이 받아올 필요가 없음. 배열 돌면서 값만 있으면 되니까.

재배열할 상태에는 구현해야하는 모양 그대로 집어넣어줘야함.
변동이 있는 값만 배열에 넣어 저장해주고
재배열 시 {v.name}으로 꺼내 바꿔줄 수 있음
가장 상위 태그에 key값 꼭! 넣어주기. 웬만하면 index보단 고유 id가 있는게 좋음(지우거나 추가돼 인덱스 바뀌면 오류 발생함)

map으로 채우는데 ` value={form.name}` 이렇게 점연산자가 있는 애들은 어떻게 하나요?
`form.name = form[name]` 이 두 값이 같다는 것을 활용해
`value={form[v.name]}` 이렇게 사용해 줄 수 있다.

useEffect(실행할 함수)
```
useEffect(()=> {
    setName: name,
    setEmail: email,
})
```
이런 형태. 이펙트가 발생하면 함수를 실행해달라 부탁하는 것.
useEffect 없으면 이벤트 발생도 전에 값을 미리 바꿔버릴 수도 있음

빈 값일 때는요???
```
useEffect(()=> {
    if(name)
    setName: name || "",
    setEmail: email || "",
})
```
if문으로 name이 있을 때 만 실행하도록 할 수 있고,
name, email이 있으면 채우고 없으면 빈 문자열로 채워주세요도 가능


onSubmit
값 담아 전송할 때 사용
form에 onSubmit={함수}를 넣어주고
button type="submit"으로 지정해줌
이떄!! button은 꼭 form안에 들어있어야함. ->onSubmit에 값 넘기기 위해서

onSubmit이나 onClick등 이벤트 발생시 실행할 함수에는 반드시
**e.preventDefault()** 넣어줘야함
기존 input이나 button이 가진 자동으로 화면 넘어가는 특성을 억제시켜줌


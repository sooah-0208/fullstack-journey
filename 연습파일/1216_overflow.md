[1216.zip](https://github.com/user-attachments/files/24188051/1216.zip)

# 💡overflow
1. `.img2{}`
  - `position: relative;`  
    `margin-top: 15px;` 이 두가지로 `Jane%John`아래 이미지 정렬함
2. `.btwrap{}`
  - `position: fixed;`로 하단 버튼부 화면 이동에 상관없이 자리 고정함(계속 화면에 떠있음)


# 💡 image 
`filter: grayscale(70%)`로 흑백 설정

# 💡 button 
1. `class abs`로 묶은 버튼이 배경/폰트 등 변경이 안되는 오류 발생
   - button 속성은 button에 따로 해야하는 것을 깨닫게됨
   - **but!** `button{}`에 속성을 넣으면 abs에 넣는 코드를 다시 넣어줘야함 -> 반복적인 코드 발생
   - 그래서 최종적으로 `.abs button{}`을 새로 만들어줌


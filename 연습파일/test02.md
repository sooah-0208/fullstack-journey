# 💡Chat GPT 제공 문제

- 가로로 박스 4개 만들기.
- 각 박스 높이는 120px, 색은 각기 다르게 지정
- 두 번째 박스만 두 배 너비, 나머지 박스는 동일 너비로 1 : 2 : 1 : 1 비율로 배치
- 세 번째 박스 안에는 글자를 넣고, 글자를 가로·세로 중앙 정렬
- 첫 번째 박스에 마우스를 올리면 배경색이 살짝 밝아지도록 hover 효과 넣기
- 모든 박스 사이에 10px 간격(margin 없이) 두기 → gap 사용

# 1차 답
```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    *{box-sizing: border-box;
        margin: 0;
        padding: 0;}
    .box{display: flex;
        width: 100vh;
        height: 100px;
        flex-grow: 1;
        gap: 10px;}
    .box1{background-color: aquamarine;
        flex-grow: 1;}
    .box2{background-color: rgb(255, 191, 221);
        flex-grow: 2;}
    .box3{background-color: rgb(191, 174, 255);
        display: flex;
        justify-content: center;
        align-items: center;
        flex-grow: 1;}
    .box4{background-color: rgb(212, 255, 94);
        flex-grow: 1;}
    
</style>
<body>
    <div class="box">
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3">안녕여러분</div>
        <div class="box4"></div>
    </div>
</body>
</html>
```

# 💦오류 체크
1. `.box`의`width: 100vh;`
   vh는 height단위라서 wh를 사용하거나 %로 바꿔야함(화면 출력 오류)
2. `.box`에`flex-grow: 1;`사용
   flex-grow는 부모가 flex컨테이너일때(display: flex) 자식의 공간 차지를 결정하는 속성임.  
   즉 `.box`는 부모 컨테이너라 상위 컨테이너가 없기때문에 의미 없는 코드  
   =>삭제해야함
4. `.box1~box4`에서 `flex-grow`사용
   구조 문제는 없으나 `flex: 1`/`flex: 2`처럼 단축 속성으로 사용하면 더 깔끔함

# 🌞최종 답변🌞
```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    *{box-sizing: border-box;
        margin: 0;
        padding: 0;}
    .box{display: flex;
        width: 100%;
        height: 100px;
        gap: 10px;}
    .box1{background-color: aquamarine;
        flex: 1;}
    .box2{background-color: rgb(255, 191, 221);
        flex: 2;}
    .box3{background-color: rgb(191, 174, 255);
        display: flex;
        justify-content: center;
        align-items: center;
        flex: 1;}
    .box4{background-color: rgb(212, 255, 94);
        flex: 1;}
    
</style>
<body>
    <div class="box">
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3">안녕여러분</div>
        <div class="box4"></div>
    </div>
</body>
</html>
```
   

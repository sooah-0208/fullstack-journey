# ⭐ 기초 Flex 연습 문제
- 문제 1: 가로로 박스 3개 만들기 / 가로로 나란히 배치 / 모두 같은 너비 / 높이는 150px / 색은 각각 다르게  
- 문제 2: 첫 번째 박스만 2배 너비 / flex-grow 사용 / 1 : 2 : 1 비율로 나누기  
- 문제 3: 가운데 박스만 세로 중앙 정렬하기 / 부모는 flex / 가운데 박스 안의 글자를 세로·가로 정가운데

# 🌞정답🌞
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{box-sizing: border-box;}   /요소 전체 크기 계산에 padding+border+내용 포함)=> 크기 계산 쉬워짐
        html,body{margin: 0; padding: 0;}   /화면에 여백 없앰/
        .box{display: flex;   /display 크기에따라 크기 변동/
             flex-grow: 1;    /남는 공간을 flex-grow비율로 나눔/
             height: 150px;
             justify-content: center;  
             align-items: center;}    
        .b1{background-color: aliceblue;}
        .b2{background-color: beige; flex-grow: 2;} 
        .b3{background-color: rgb(255, 199, 199);}
    </style>
</head>
<body>
    <div class="box">
        <div class="box b1">하나</div>
        <div class="box b2">둘</div>
        <div class="box b3">셋</div>
    </div>
</body>
</html>
```
<img width="609" height="339" alt="image" src="https://github.com/user-attachments/assets/afb98e37-c8f4-4629-aefc-424d33864539" />

# 💡iframe  
- 지도, 영상, 웹 페이지 등의 링크를 복사하여 웹페이지 화면에 그대로 띄워내기 위한 코드  
- 기존 페이지에서 사용하는 기능을 그대로 가져올 수 있음  
- width / height / style등 직접 지정해야함  
- 대시보드에 각 화면을 `iframe`으로 불러오는 방식 사용함  
- Why? 각 화면마다 각각 불러오기 때문에 부화를 줄여줄 수 있음  
- `allowfullscreen=""`: 전체화면 허용 `""` 값이 비어있어도 허용됨
- `loading="lazy"`: 지연 로딩: 화면에 보이기 전까진 로딩하지 않음(페이지 속도 개선에 도움이 된다.)
- `referrerpolicy="no-referrer-when-downgrade"`
  - 참조(referrer) 정보 전달 규칙
  - 의미: HTTPS → HTTPS : referrer 전달
          HTTPS → HTTP : referrer 전달 안 함 (보안상 안전)

# 💡선택자
style에서 사용하는 항목  
우선순위: !important > inline(tag에 직접 입력한style) > tag+class+id > id(#) > class(.) > tag  

### 🔹예시
*css*

```
p { color: blue;
background-color: white !important; }
.text { color: green;
background-color: black; }
#title { color: orange; }

```
*html*
```
<p id="title" class="text" style="color: red;">
  Hello
</p>
```
이렇게 넣으면 최종적으로 `배경색 black / 글씨색 red`가 채택됨  



## 🔹span
- span{]을 여러개 설정하면 마지막 설정만 적용됨
- div>span {]은 div 자식으로 들어간 span에 적용되기에 위랑 다르게 적용 가능함
- #ex span: ex는 id // div id가 ex인 것 중 span항목에 적용  
🤔 div.first-class>span{background-color: #ff0;]   
		#ex span{background-color: aqua;]  
  얘는 왜 aqua만 적용되나요??  
  => span의 기본 속성! 마지막 설정만 적용되는 속성 때문!  

### 🔹선택자 사용법 `[]`
- 기본 형태a[href?="?"]{?}"`  
- = 전체 일치  
- ^= 시작하는
- $= 끝나는
- *= 일부 문자 (단어 중 일부 문자)
- ~= 단어 일치
  
```
a[href^="https"] {background-color: purple; color:#fff;}
a[href$="net/"]{color:red;}
li[title*="ip"]{color:aqua;}  

⭐해석: https로 시작하는 항목은 보라색배경에 흰 글씨로 주세요
      net/으로 끝나는 항목은 빨간 글씨로 주세요
      title항목에 ip라는 글자를 포함하면 아쿠아색 글씨로 주세요
```

=>❓여기titletle`속성은 마우스를 올렸을 때 말풍선(툴팁)이 뜨도록 하는 속성!  

## 🔹link / button in style
text-decoration: none;ne;` 밑줄 없애는 속성  
a:hover{}r{}` 마우스를 올렸을 때 스타일 설정  
a:focus{}s{}` Tab을 누르면 커서가 이동하는데 이때 커서 이동시 보이는 스타일 설정  
a:`a:` 에 `a`는 링크이기 때문에 다른 항목에 주고싶으면 `:`앞`div/p/li/li`등으로 바꿔주면 됨
```
/* 방문하지않은 link */
*	a:link{color:#0f0;
			text-decoration: none;}

/* 방문한 link */
*	a:visited{color: #ddd;}

/* 마우스를 올려 놨을 때 */
*	a:hover{color: #f00;
			text-decoration: underline;}

/* 클릭했을 때 */
*	a:active{color: #00f;}

/* 탭키 */
*	a:focus{background-color: #ff0;}
```

## 🔹~를 찾아서 적용 `(?): :(?)`
- 선택자 앞/뒤 스타일 변경 after/beforeore `(h1): :beforeore / (h1): :afterter`의 형식으로 적용
- 드래그 했을 때:`selectionion`
- 첫 글자만:`first-letterter`
- 등등 다양한 선택자가 존재함

# 🔹size 조절
## [단위]  
절대값 단위(인쇄용)     : cm, mm, pt(포인트), pc(파이카)  
상대값 단위(웹, 스크린) : px(1픽셀을 1로 하는 단위),  
						em(~배, 상위 요소 기준),  
						rem(~배, 최상위 요소[html] 기준, HTML5 추가)  
						%(비율, 상위 요소 기준)  

# 🔹font 속성 `font-(?)`
- size: `[단위]`랑 같음
- family: 폰트 지정
- weight: 두께(bold/normal이나 숫자로 직접 설정도 가능함. 400이 normal, 600이 bold)
- style: 기울임(`italic`폰트에 정의된 기울임/`oblique`그냥 기울인 글자)
- variant-caps: 글자의 표현 방식 변형(small-caps: 소문자를 작은 대문자로/다른 값도 있지만 폰트가 지원 안 하는 경우가 많아 잘 안 씀)
- line-height: font-size기준으로 줄 높이를 결정함
  1) **숫자(1.5, 1.2, 2 ...)**: 가장 추천/ 부모에 비례하기 때문에 반응형에 좋음
  2) px: 고정된 값 / 정확하지만 유연성이 떨어짐
  3) %: 잘 안 씀
  4) normal: 브라우저 기본값(보통 1.2~1.4)
  예시
  ```
  p {font-size: 16px;
  line-height: 1.5;}
  ```
### 🔹텍스트가 한 줄 일 때 가운데 정렬하는 방법
```
.box {
  height: 50px;
  line-height: 50px;}
```
👉 한 줄 텍스트일 때만 사용 (여러 줄 ❌)

# 💡영역  

## 1️⃣overflow 

- 요소 안의 내용이 넘칠 경우 어떻게 처리할지 정하는 CSS속성  
	=> 부모보다 자식이 클 때 처리방식  
-`overflow: 값;` 
-`hidden`: 넘치는 부분 잘리게 표현(스크롤 ❌)
- `scroll`: 내용이 적어도 항상 스크롤바 표시
- `auto`: 넘칠 때만 스크롤바 생성(실무에서 가장 많이 사용)

## position
HTML 요소를 '어디에, 어떤 기준으로 배치할지' 정하는 CSS 속성  
`position: 값;` 형태  
top / left / right / bottom 기준을 정해주는 속성  
레이어처럼 배경 내용 위에 쌓여 올라감  

1️⃣ static (기본값)
- 위치 이동 안 됨: top, left 등 인식 안 됨
- 공간이 그대로 남아있음

2️⃣ relative
- 기존 영역 그대로 차지함
- top/left 값을 줘야만 이동함(relative만 주면 아무 변화가 안 생김)
- 원래 자기 위치에서 이동 => 즉, static 기준으로 이동
- 공간은 그대로 남아있음
- **absolute의 기준점 역할로 자주 사용**

3️⃣ absoulute
- 기존 영역 인식 안 함(배경과 겹치게 됨) 
- 상위 엘리먼트 기준으로 이동
  relative / absolute / fixed / sticky 중 하나면 기준이 됨
  ❌ static 부모는 무시
  👉 없으면 body(= 문서) 기준
- 상위 엘리먼트가 body 일 경우, 웹 브라우저 기준
  
4️⃣ fixed
- absoulate 와 비슷
- 화면이 스크롤 되어도 그 위치 그대로
- 무조건 웹 브라우저 기준
- 보통 광고화면 계속 노출시킬 때 쓰기도 함

5️⃣ sticky(relative+fixed느낌)
- 화면이 스크롤 되어도 그 위치 그대로(부모 영역 안에서만)
- 보통 광고화면 계속 노출시킬 때 쓰기도 함

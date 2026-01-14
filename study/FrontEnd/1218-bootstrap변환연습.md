# 🥨CSS->Bootsrap 변환
기존 파일은 손대지 않기!!
원본 파일은 보존해놓고 복사본으로 bootstrap 으로 변경해가며 확인하기

## 1️⃣ head에 link 연결해주기
순서 정리  
1. Bootstrap  
   `<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
  rel="stylesheet">`
2. 공통 css
   `<link rel="stylesheet" href="css.css">`
3. 페이지 전용 css  
   `<link rel="stylesheet" href="main.css">`
4. JS
   `<script src="movie.js" defer></script>`  

🎉**왜냐면** CSS는 아래가 위를 덮기때문에 우선순위를 **내림차순**으로 정리해줘야함

## 2️⃣ Bootstrap시 충돌나지 않도록 class명 정리하기
- `btn`,`p`등과 같이 bootstrap에 있는 개념의 class를 변경.
- ctrl+H 눌러 Find+Replace 창 열면 하나 찾고 전부 바꿀 수 있음
- 원래는 임의대로 class 명을 정했는데 실무에서 쓰는 class명이 있다는 것을 알고 변경.
- 🎉**CSS class 나열방식**: `first .title .exps`처럼 모든 css를 사용할 때 큰 부모>부모>자식 형식으로 포함시켜야하는 줄 알고 전부 나열식으로 작성하였음 -> 그러나 하위 자식의 class는 겹치고, 부모 class가 다를 때 사용한다는 것을 알았음 => 최종적으로 파일 css 정리함
```
기존
.main .movie_lists .movie_list .list_text{}
1차 변경 후
.movie-main .movie-list .movie-item{}
최종 변경
.movie-item{}
```
## 3️⃣ CSS에서 Bootstrap으로 대체 가능한 파트 찾기
- d-flex / d-block ,w/h-100 = class display: flex / displayl: block, height: 100% 등
- **변경되지 않는 부분은 기존 CSS 그대로 유지함**

## 4️⃣ 웹 화면 체크
알맞게 변형되는지 변동사항 확인하며 Bootstrap class로 변경

## 완성~!~!

# movie action하게 만들기
javascript 이용하여 화면 내용 바뀌게 만들기
- OMBb API에서 소스 얻어옴(key 받아오기)  
이거는 나중에 자바스크립트 배울 때 코드 짜는 법 배울고에용~~

# html 추가

```
<head>
<script src="js주소"></script>
</head>
<body onload="load()">

<form action="#" class="search-box" id="movie-search">
  <input type="text" name="keyword" placeholder="영화 제목을 입력하세요." />
  <input type="submit" value="검색" />
</form>

</body>
```


# js코드
```
function view(list) {
  let html = "";
  for(const row of list) {
    html += `<div class="movie">
              <a href="movie.html" class="movie-link">
                <div class="product-image">
                  <img src="${row.Poster}" alt="Movie Poster"/>
                  <div class="type">${row.Type}</div>
                </div>
                <div class="detail">
                  <p class="year">${row.Year}</p>
                  <h3>${row.Title}</h3>
                </div>
              </a>
            </div>`;
  }
  document.querySelector(".movies-list").innerHTML = html;
}
function movies(keyword) {
  const url = `https://www.omdbapi.com?apikey=2815efbb&s=${keyword}`;
  fetch(url)
  .then(x => x.json())
  .then(y => {
    if(y.Response === 'True') view(y.Search);
  });
}
function submit(e){
  e.preventDefault();
  const keyword = e.target.keyword.value;
  if(keyword) movies(keyword);
}
function load() {
  document.getElementById("movie-search").addEventListener("submit", submit);
}
```
여기서 class명-> 내 파일 class로 바꿔주면 됨
지금 예시는 movie화면용으로 만들어진 예시

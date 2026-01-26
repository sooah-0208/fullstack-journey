React

react 실행 방법
node.js가 깔려있어야 가능함
실행하려는 폴더로 들어감
상단에 cmd 입력하여 명령 프롬포트 on
`npm create vite@latest 원하는 폴더명`입력
프레임워크 React 선택
Javascript 선택
Use rolldown-vit (Experimental)? - no
다음 질문 yes 하면 다운 시작 됨
선택한 폴더에 자동으로 react파일 생성 완료
로컬 서버 컨트롤 + 클릭해서 열면 확인 가능
cmd에서 바로 vsCode 켜는 법: 폴더명 입력 후 엔터 -> code . 입

class Abc
Abc라는 클래스(설계도)를 만드는 메소드
첫 글자는 무조건 대문자!!
html에서 태그에 class 달아준 거랑 같은 의미라고 생각하면 됨

constructor(){}
클래스에 객체를 만들 때 자동 실행되는 함수

객체란? 
이름표가 붙은 여러개의 값 묶음
```
const car = {
  brand: "Hyundai",
  color: "white",
  door: 4,
  drive: function () {
    console.log("출발!");
  }
};
```

객체에서 값 꺼내는 방법
변수명.속성(데이터명)
car.brand   //"Hyundai"
car.door    //"4"
car.color   //"white"
like that.

객체가 왜 필요한가요?
없이 let으로 설정할 경우
```
let brand = "Hyundai";
let color = "white";
let door = 4;
```
서로 관계있는 값임에도 불구하고 따로 놀게 됨
`const car = {내용};`으로 묶으면 한 덩어리로 관리 가능

객체는 여러개 제작 가능함
const car1 = {brand: "BMW", color: "white"};
const car2 = {brand: "Hyundai"};


but 매번 객체를 직접 쓰면 번거로움
=>>>> 그래서 설계도(=class)가 필요함

```
class Car{
  constructor(brand){       // *참고
    this.brand = brand;
  }
}     // ^^^ 객체 만드는 툴
```
*constructor: 클래스로 객체를 만들 때 딱 1번 자동 실행되는 함수
`new`를 쓰는 순간 자동 실행
`new Car("Hyundai");`를 입력하면
Car에 새 객체로 "현대"를 넣어줌 -> 이 객체는 brand에 들어감
-> 즉 brand === "Hyundai"

그럼 constructor에 여러 값을 받고싶어요!
constructor는 클래스당 **1개만 가능**
**매개변수로 여러 값** 받을 수 있음
```
class Car{
  constructor(brand, color, door){
    this.brand = brand;
    this.color = color;
    this.door = door;
  }
}

const car1 = new Car("현대", "흰색", 4);
const car2 = new Car("롤스", "검정색", 2);
```
위와 같은 형태로 입력 가능함

콘솔로 찍어보면 확인 가능
```
console.log(car1.color);   //흰색
console.log(car1);         //car{"현대", "흰색", 4}
console.log(car2.brand);   //롤스
```
`new`
class의 constructor에 새 값을 넣겠다는 의미
위 예시에서 보면 
new Car 뒤에 들어간 내용이 위 Car class에 각각 새로운 값으로 채워져서
출력하면 new이하의 값이 출력됨.


`extends` & `super`
extends
자식 extends 부모 -> 자식을 부모 아래로 상속시키기 위한 메소드
super
부모의 constructor를 실행하라는 명령어
->부모 class의 constructor를 지금 이 객체(this)기준으로 실행하라는 의미
->그래서 super 이후에 this가 꼭 들어가야함
<img width="924" height="444" alt="image" src="https://github.com/user-attachments/assets/1e7ae173-d45e-4f5b-8d58-91be50238777" />

->brand는 부모 Car에서 그대로 받아와서 "현대"가 들어가고
색은 Color에 넣어줬기 떄문에 "흰색"으로 나옴

class Model extends Car => Model을 Car 자식으로 넣음


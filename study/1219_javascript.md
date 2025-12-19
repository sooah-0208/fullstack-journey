# Javascript(ECMAScript)
- 객체 지향 프로그래밍 OOP
- `JS` 혹은 `ES`라고 부름
- 주로 frontend에 사용하는 프로그램(백엔드엔 한계가 있음)

script의 src 확인하는 방법: 콘솔->Sources->js파일

script도 body처럼 스크립트 순서대로 출력이 됨
```
<script>어쩌구</script>
<script>저쩌구</script>

=>어쩌구저쩌구
```

## 자료형
### [기본 타입] Primitive Type
		- number    : 숫자(정수, 실수)
		- bigint    : 정수 -(2의 53승 -1) ~ 2의 53승-1
		- string    : 문자열
		- boolean   : 논리값(true, false)
		- undefined : 초기화되지 않은 상태(함수에서 출력값이 없을 때), 변수 초기화에 사용(변수에서 입력값이 없을 때) ==>javascript에서만 사용됨!
		- null      : 객체 변수 초기화 사용
		- NaN       : Not a Number(영역에 숫자가 들어가지 않았을 때(문자열이 들어있을 때)  
    **number, 특수기호 ⊂ string** => 그래서 숫자가 포함된 문자열은 문자열로 봄    
    ->그럼 왜 숫자열과 문자열이 나눠져있나요? = 계산을 하기 위해서. 문자열은 계산식에서 제외됨  
		5+1=6  
		5+"1"=51('5'와'1'을 다 문자로 봐서 계산이 안됨)  

### [참조 타입] 참조형, Reference Type
		- array
		- function
		- ...

### [변수선언]
 var 변수명; (형식)
```
var num;
document.write('num >>' +num);
document.write('<br>');
document.write('num type >>', typeof num);
document.write('<br>');
```

typeof: 변수가 가진 자료형이 뭐인지

#### 값 비교시
==: 안에 요소만 비교
===: 자료형도 비교
ex) 5=="5": true
    5==="5": false


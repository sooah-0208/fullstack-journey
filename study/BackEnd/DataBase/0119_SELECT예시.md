Schema 부르는 방법

`USE edu;`
원하는 데이터베이스 선택

```SELECT * FROM edu.departments```

-- 1.사원 이름, 성별 추출
```
SELECT first_name, last_name, gender 
FROM edu.employees;
```

SELECT: 테이블에서 원하는 COL명만 추출
FROM: COL이 있는 테이블

-- 2.  사원의 사원 번호, 연봉 추출
```
SELECT salary, emp_no 
FROM edu.salaries;
```

-- 3. 부서의 번호, 부서명 추출
```SELECT *FROM edu.departments;```

-- 4. 사원의 이름과 연봉 추출
-- employees,salaries
```
SELECT e.first_name, 
		 e.last_name,
	    s.salary
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
ON (e.emp_no = s.emp_no)
;
```
JOIN: 두개 이상의 테이블을 공통된 COL기준으로 합쳐줌
- 여기서는 `emp_no`가 양쪽 테이블에 같이 있어서 합쳐준거임

INNER JOIN: 
ON: 

-- 5. 사원 중 남자의 연봉 추출
```
SELECT e.first_name, 
		 e.last_name,
		 e.gender,
		 s.salary
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
ON (e.emp_no = s.emp_no)
WHERE e.gender <> 'M';
```
WHERE: 조건식
비교연산자 사용 가능
`!=` = `<>` NOT은 이렇게 두개로 적을 수 있음

-- 6. 여성 사원중 연봉이 7만 이상인 사원 추출
```
SELECT e.first_name, 
		 e.last_name,
		 e.gender,
		 s.salary
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
ON (e.emp_no = s.emp_no)
WHERE e.gender = 'F'
AND s.salary > 70000
AND s.to_date = '9999-01-01';
```
AND: 여러 조건을 만족해야하는 경우

-- 7. 여성사원 중 연봉 협상이 가장 많은 사원 추출
```
SELECT emp_no, COUNT(emp_no) AS cnt
FROM edu.salaries
GROUP BY emp_no
ORDER BY 2 DESC, 1;
```

- `COUNT()` 카운트: 행(row)의 개수를 세는 집계 함수
null이 아닌 행만 세어줌  
- `GROUP BY`: 같은 값의 행들을 하나의 그룹으로 묶음
❌ 이게 없으면 에러 남  
👉 emp_no는 개별 값  
👉 COUNT(emp_no)는 집계 결과  
👉 같이 쓰려면 그룹 기준이 필요  
emp_no별로 묶은 후 그 묶음마다 카운트를 계산함

📌 결과:
```
emp_no = 10001 → 17개
emp_no = 10002 → 1개
```


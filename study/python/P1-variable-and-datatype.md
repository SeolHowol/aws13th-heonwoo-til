# 변수
## 변수?
> 값을 저장하는 메모리 공간에 붙이는 이름
### 1. 값 저장
> 프로그램에서 사용할 데이터를 변수에 저장
```
user_name = "철수"
```
### 2. 값 사용
> 저장한 값을 변수 이름을 통해 사용
```
# 화면에 출력
print(user_name)
print("안녕하세요," + user_name + "님!")

# 다른 변수에 복사
greeting_target = user_name
```
### 3. 값 변환
> 프로그램 실행 중에 상황이 바뀌면 변수의 값도 변경 가능
```
user_name = "영희"
print(user_name)
```

## 변수 선언과 할당
### 1. 기본 문법
```
변수명 = 값
```
> 오른쪽의 값을 왼쪽 변수에 넣는다
### 2. 변수 이름 규칙
> 변수의 선언을 위해서 지켜야 할 규칙

| 규칙 | 올바른 예 | 잘못된 예 |
| --- | --- | --- |
| 문자 또는 밑줄(`_`)로 시작 | `name`, `_count` | `1name`, `@user` |
| 숫자로 시작 불가 | `user1` | `1user` |
| 공백 사용 불가 | `user_name` | `user name` |
| 예약어 사용 불가 | `my_class` | `class`, `if`, `for` |

## 변수를 활용한 연산 및 할당
### 1. 산술 연산 
```
price = 1000
quantity = 3

total = price * quantity
```
### 2. 문자열 연결
```
first_name = "김"
last_name = "개발"

full_name = first_name + last_name

print(full_name)  # 출력: 김개발
```
### 3. 복합 할당 연산
```
count = 10

# 긴 방식
count = count + 1

# 짧은 방식 (동일한 결과)
count += 1
```
| 연산자 | 의미 | 예시 |
| --- | --- | --- |
| `+=` | 더하고 저장 | `x += 5` → `x = x + 5` |
| `-=` | 빼고 저장 | `x -= 3` → `x = x - 3` |
| `\*=` | 곱하고 저장 | `x \*= 2` → `x = x \* 2` |
| `/=` | 나누고 저장 | `x /= 4` → `x = x / 4` |

### 4. 다중할당
```python
name, age, city = "철수", 25, "서울"
print(name)  # 출력: 철수
print(age)   # 출력: 25
print(city)  # 출력: 서울
```
### 5. 값 교환
```python
a = 10
b = 20

# 파이썬 방식: 한 줄로 교환
a, b = b, a

print(a)  # 출력: 20
print(b)  # 출력: 10
```

# 자료형 (Data Types)
## 자료형이란?
> 변수에 저장되는 데이터의 종류

### 1. 정수형(int)
> integer의 약어, 소수점 없는 숫자

### 2. 실수형(float)
> floating point의 약어, 소수점이 있는 숫자

### 3. 문자형(string)
> 문자들의 열, 따옴표로 감싸진 문자들의 나열 (큰 따옴표, 작은 따옴표 구분 X)

- 이스케이프 문자

| **이스케이프** | **의미** | **예시** |
| --- | --- | --- |
| `\\n` | 줄바꿈 | `"Hello\\nWorld"` → Hello (줄바꿈) World |
| `\n` | 탭 | `"Hello\nWorld"` → Hello (줄바꿈) World |
| `\t` | 백슬래시 | `"A\tB"` → A    B |
| `\\` | 작은따옴표 | `"C:\\Users"` → C:Users |

### 4. f-string (포메팅)
```
name = "철수"
age = 25

# f-string 사용
message = f"이름: {name}, 나이: {age}세, 키: {height}cm"
message = f"이름: {name}, 나이: {age}세"
print(message)  # "이름: 철수, 나이: 25세"
# 표현식도 사용 가능
print(f"내년 나이: {age + 1}세")  # "내년 나이: 26세"

# 소수점 자릿수 지정
pi = 3.141592653589793
print(f"원주율: {pi:.2f}")  # "원주율: 3.14" (소수점 2자리)
print(f"원주율: {pi:.2f}")  # "원주율: 3.14"
```

### 5. 논리형 (Boolean)
> 참 또는 거짓 구분 (True, False)

- 논리 연산자

| **연산자** | **의미** | **예시** |
| --- | --- | --- |
| `and` | 둘 다 참이면 참 | `True and False` → `False` |
| `or` | 하나라도 참이면 참 | `True or False` → `True` |
| `not` | 반대로 뒤집기 | `not True` → `False` |

### 6. None 타입
> 값이 없음 (null)


## 형 변환
```
# 문자열 → 정수
num_str = "123"
num_int = int(num_str)
print(num_int + 1)  # 124

# 문자열 → 실수
price_str = "99.99"
price_float = float(price_str)
print(price_float * 2)  # 199.98

# 숫자 → 문자열
age = 25
age_str = str(age)
print("나이: " + age_str)  # "나이: 25"
```

## input의 형변
```
user_input = input("숫자를 입력하세요: ")  # "42" (문자열!)

# ❌ 잘못된 사용
# result = user_input + 10  # TypeError!

# ✅ 올바른 사용
number = int(user_input)
result = number + 10
print(result)  # 52
```

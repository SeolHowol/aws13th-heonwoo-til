# 느낌 있는 파이썬의 시작

## 변수
> naming convention
- 회사 및 사회에서 공유하는 변수의 공통된 규칙성
1. 숫자로 시작 금지
2. 공백 사용 불가
3. 예약어 사용 불가
   
> 정수형 (int)
- integer의 줄임말
- 양수, 0, 음수 포함 정수
```
a = 3
```
> 실수형 (float)
- floating point의 줄임말
- 소수점이 있는 숫자
```
a = 2.313
```
> 문자열(str)
- String
- 따옴표로 감싸진 문자들
```
name = "김철수"
```
- 삼중 따옴표 가능 '''

|이스케이프|의미
|------|------|
|\\n|줄바꿈|
|\n|탭|
|\t|벡슬래쉬|
|\\ \\ |작은따옴표|
> f-string
```
name = "철수"
age = 25

> f-string 사용
message = f"이름: {name}, 나이: {age}세, 키: {height}cm"
message = f"이름: {name}, 나이: {age}세"
print(message)  # "이름: 철수, 나이: 25세"
```
> 논리형 (Bool)
- Boolean
```
is_student = True
has_license = False
```
- 비교 연산
```
a = 10
b = 5

print(a > b)   # True  (a가 b보다 크다)
print(a < b)   # False (a가 b보다 작다)
print(a == b)  # False (a와 b가 같다)
print(a != b)  # True  (a와 b가 다르다)
```
- 논리 연산자

| 연산자| 의미 | 예시 |
| --- | --- | --- |
| `and` | 둘 다 참이면 참 | `True and False` → `False` |
| `or` | 하나라도 참이면 참 | `True or False` → `True` |
| `not` | 반대로 뒤집기 | `not True` → `False` |

> None
- 값이 없음
- "" (빈 문자열): 상자는 존재
- None: 상자 자체가 없음
- 일단 적어두고 다시 공부 필요!!!
```
def greet(name):
    print(f"Hello, {name}!")
    # return이 없음 → 자동으로 None 반환

result = greet("철수")  # "Hello, 철수!" 출력
print(result)           # None

result = None
print(type(result))  # <class 'NoneType'>

value = None

# ✅ 권장: is 연산자 사용
if value is None:
    print("값이 없습니다")

# ❌ 비권장: == 연산자 (동작하지만 권장하지 않음)
if value == None:
    print("값이 없습니다")
```

### 기타사항
> 변수 변환 (재할당)
```
user_name = "철수"
user_name = "영희"
```
> 정수 가산
```
x += 1
```
> 값 교환
```
a, b = b, a
```
> 동시할당
```
name, age, city = "철수", 25, "서울"
```
> type 출력
```
print(type(age))
```
> 명시적 형변환
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
## 입출력
> print()
```
print({변수})
print("Hello" + {변수} + "Sir")
```
> input
```
user_input = input("숫자를 입력하세요: ")  # "42" (문자열!)

# ❌ 잘못된 사용
# result = user_input + 10  # TypeError!

# ✅ 올바른 사용
number = int(user_input)
result = number + 10
print(result)  # 52
```
## 자료형

- 여러 값을 담든 것을 컬렉션 자료형

| 자료형 | 일상의 물건으로 빗대어보면.. | 핵심 특징 |
| --- | --- | --- |
| 리스트 | 할 일 목록 | 순서대로 적고, 언제든 추가/삭제 가능 |
| 튜플 | 밀봉된 택배 | 순서는 있지만, 한 번 포장하면 못 바꿈 |
| 딕셔너리 | 사전책 | 단어(키)로 뜻(값)을 찾음 |
| 세트 | 당첨 번호 주머니 | 순서 없이 담고, 중복 없음 |
| 문자열 | 목걸이 구슬 | 글자가 순서대로 연결됨 |

> 리스트(list)
- 여러 개의 값을 **순서대로** 저장
```
# 대괄호 []로 만들어요
fruits = ["사과", "바나나", "딸기"]
numbers = [1, 2, 3, 4, 5]
mixed = ["철수", 25, True]  # 다른 종류도 섞을 수 있어요!
```
- 온라인 쇼핑몰 예시
```
# 빈 장바구니로 시작
cart = []

# 상품 담기
cart.append("노트북")
cart.append("마우스")
cart.append("키보드")

print(cart)  # ['노트북', '마우스', '키보드']
```
- 리스트에서 값 꺼내기
```
fruits = ["사과", "바나나", "딸기", "포도"]
#          0번     1번      2번     3번
print(fruits[0])   # 사과 (첫 번째)
print(fruits[1])   # 바나나 (두 번째)
print(fruits[-1])  # 포도 (마지막! -1은 뒤에서 첫 번째)
```
- 리스트 수정하기 
```
# 📋 쇼핑 목록으로 연습해볼게요
shopping = ["우유", "빵"]

# ➕ 추가하기 (Create)
shopping.append("계란")           # 맨 뒤에 추가
print(shopping)  # ['우유', '빵', '계란']

shopping.insert(1, "치즈")        # 1번 위치에 끼워넣기
print(shopping)  # ['우유', '치즈', '빵', '계란']

# 👀 읽기 (Read)
print(shopping[0])    # 우유
print(len(shopping))  # 4 (몇 개 있는지)

# ✏️ 수정하기 (Update)
shopping[0] = "저지방우유"        # 0번을 바꾸기
print(shopping)  # ['저지방우유', '치즈', '빵', '계란']

# 🗑️ 삭제하기 (Delete)
shopping.remove("치즈")           # 값으로 삭제
print(shopping)  # ['저지방우유', '빵', '계란']

last_item = shopping.pop()        # 마지막 꺼내기
print(last_item)  # 계란
print(shopping)   # ['저지방우유', '빵']
```
- 리스트 method
  
| 메서드 | 하는 일 | 예시 |
| --- | --- | --- |
| `append(x)` | 맨 뒤에 x 추가 | `list.append("새값")` |
| `insert(i, x)` | i번 위치에 x 끼워넣기 | `list.insert(0, "맨앞")` |
| `remove(x)` | x 값 삭제 (첫 번째만) | `list.remove("삭제할값")` |
| `pop()` | 마지막 값 꺼내기 | `last = list.pop()` |
| `sort()` | 오름차순 정렬 | `list.sort()` |
| `reverse()` | 순서 뒤집기 | `list.reverse()` |
| `len(list)` | 길이(개수) 확인 | `print(len(list))` |

> 딕셔너리
- 딕셔너리는 이름표(키)를 붙여서 값을 저장하는 방식
```
contacts = {
    "엄마": "010-1234-5678",
    "아빠": "010-8765-4321",
    "친구": "010-1111-2222"
}

# 이름으로 전화번호 찾기
print(contacts["엄마"])  # 010-1234-5678
```
- 딕셔너리 수정하기
```
# 📖 연락처 앱으로 CRUD 연습해볼게요
contacts = {}

# ➕ 추가하기 (Create)
contacts["엄마"] = "010-1234-5678"      # 새 키-값 추가
contacts["아빠"] = "010-8765-4321"
print(contacts)  # {'엄마': '010-1234-5678', '아빠': '010-8765-4321'}

# 여러 개 한 번에 추가하기
contacts.update({"친구": "010-1111-2222", "회사": "02-123-4567"})
print(contacts)
# {'엄마': '010-1234-5678', '아빠': '010-8765-4321', '친구': '010-1111-2222', '회사': '02-123-4567'}

# 👀 읽기 (Read)
print(contacts["엄마"])           # 010-1234-5678
print(contacts.get("여동생"))     # None (없어도 에러 안 남)
print(contacts.get("여동생", "번호 없음"))  # 번호 없음 (기본값)
print(len(contacts))              # 4 (몇 개 있는지)
print("엄마" in contacts)         # True (키가 있는지 확인)

# ✏️ 수정하기 (Update)
contacts["엄마"] = "010-9999-8888"  # 기존 키에 새 값 덮어쓰기
print(contacts["엄마"])  # 010-9999-8888

# 🗑️ 삭제하기 (Delete)
del contacts["회사"]               # 키로 삭제
print(contacts)  # {'엄마': '010-9999-8888', '아빠': '010-8765-4321', '친구': '010-1111-2222'}

removed = contacts.pop("친구")     # 삭제하면서 값 받기
print(removed)    # 010-1111-2222
print(contacts)   # {'엄마': '010-9999-8888', '아빠': '010-8765-4321'}

contacts.clear()                   # 전부 삭제
print(contacts)   # {}
```
딕셔너리 method 

| 메서드 | 하는 일 | 예시 |
| --- | --- | --- |
| `dict[key] = value` | 키-값 추가/수정 | `contacts["친구"] = "010-0000"` |
| `update(dict2)` | 여러 키-값 한 번에 추가 | `contacts.update({"a": 1, "b": 2})` |
| `get(key)` | 안전하게 값 가져오기 | `contacts.get("엄마", "없음")` |
| `keys()` | 모든 키 가져오기 | `list(contacts.keys())` |
| `values()` | 모든 값 가져오기 | `list(contacts.values())` |
| `items()` | 키-값 쌍 가져오기 | `for k, v in contacts.items():` |
| `del dict[key]` | 키로 삭제 | `del contacts["엄마"]` |
| `pop(key)` | 삭제하면서 값 반환 | `removed = contacts.pop("친구")` |
| `clear()` | 전부 삭제 | `contacts.clear()` |

> 문자열
- 글자들이 순서대로 연결된 것
- 문자열 인덱싱
```
text = "PYTHON"
#       012345

print(text[0])   # P
print(text[1])   # Y
print(text[-1])  # N (마지막)
```
- 문자열 변환
```
text = "  Hello, Python!  "

# 대소문자 변환
print(text.upper())    # "  HELLO, PYTHON!  "
print(text.lower())    # "  hello, python!  " 

# 앞뒤 공백 제거
print(text.strip())    # "Hello, Python!"

# 특정 글자 바꾸기
print(text.replace("Python", "World"))  # "  Hello, World!  "
```
- 문자열 나누기
```
email = "[user@example.com](mailto:user@example.com)"
parts = email.split("@")  # ["user", "[example.com](http://example.com)"]
print(parts[0])  # user
print(parts[1])  # [example.com](http://example.com)
```
- f-string 문자열 안에 변수 넣기
```
name = "철수"
age = 20

# f-string 사용 (가장 쉬운 방법!)
print(f"이름: {name}, 나이: {age}세")
# 이름: 철수, 나이: 20세

# 계산도 가능해요
print(f"내년 나이: {age + 1}세")
# 내년 나이: 21세
```

> 튜플
- 한 번 만들면 **수정할 수 없는 리스트**
- **데이터 수정시 문제가 큰 경우 사용**
```
# 좌표는 바뀌면 안 되니까 튜플로!
location = (37.5665, 126.9780)  # 서울시청 위도, 경도

# 요일도 바뀌면 안 되죠
days = ("월", "화", "수", "목", "금", "토", "일")
```
- 튜플 활용하기
```
# 📦 택배 상자 내용물로 연습해볼게요 (한 번 포장하면 못 바꿔요!)

# ➕ 만들기 (Create) - 처음 만들 때만 가능!
package = ("노트북", "충전기", "마우스")
print(package)  # ('노트북', '충전기', '마우스')

# 👀 읽기 (Read) - 리스트와 똑같아요!
print(package[0])     # 노트북 (첫 번째)
print(package[-1])    # 마우스 (마지막)
print(package[0:2])   # ('노트북', '충전기') (슬라이싱)
print(len(package))   # 3 (몇 개 있는지)
print("노트북" in package)  # True (있는지 확인)

# ✏️ 수정하기 (Update) - 불가능!
# package[0] = "태블릿"  # TypeError: 튜플은 수정할 수 없어요!

# 🗑️ 삭제하기 (Delete) - 불가능!
# del package[0]  # TypeError: 튜플 요소는 삭제할 수 없어요!
```
- **언패킹** (튜플, 리스트 둘 다 가능)
```
point = (10, 20)

# 한 번에 두 변수에 담기!
x, y = point
print(x)  # 10
print(y)  # 20
```

> 세트
- **중복을 허용하지 않고, 순서가 없는** 자료형
- 활용하기
```
# 🎱 로또 당첨 번호 관리로 연습해볼게요
lotto = set()

# ➕ 추가하기 (Create)
lotto.add(7)           # 하나 추가
lotto.add(21)
lotto.add(35)
print(lotto)  # {35, 7, 21} (순서는 랜덤!)

lotto.add(7)           # 이미 있는 값은 무시됨 (중복 X)
print(lotto)  # {35, 7, 21} (그대로!)

# 여러 개 한 번에 추가
lotto.update([1, 14, 28])
print(lotto)  # {1, 35, 7, 14, 21, 28}

# 👀 읽기 (Read)
# lotto[0]  # ❌ 에러! 세트는 인덱싱 안 돼요
print(7 in lotto)     # True (있는지 확인)
print(100 in lotto)   # False
print(len(lotto))     # 6 (몇 개 있는지)

# ✏️ 수정하기 (Update)
# 세트는 개별 요소를 직접 수정하는 기능이 없어요
# 대신 삭제 후 추가하는 방식으로 해요
lotto.remove(35)      # 35 삭제
lotto.add(42)         # 42 추가
print(lotto)  # {1, 7, 42, 14, 21, 28}

# 🗑️ 삭제하기 (Delete)
lotto.remove(1)       # 값으로 삭제 (없으면 에러!)
print(lotto)  # {7, 42, 14, 21, 28}

lotto.discard(100)    # 없어도 에러 안 남 (안전한 삭제)
print(lotto)  # {7, 42, 14, 21, 28} (그대로)

popped = lotto.pop()  # 아무거나 하나 꺼내기
print(f"꺼낸 값: {popped}")

lotto.clear()         # 전부 삭제
print(lotto)  # set()
```
## 제어문
### 조건문
- 함수: if, elif, else
- 비교연산자: ==, !=, <, >
- 논리연산자: and, or, not
- 활용 예시
```
# 사용자에게 나이를 물어봐요
age = int(input("나이를 입력하세요: "))

# 나이에 따라 다른 요금을 적용해요
if age >= 65:                              # 만약 65세 이상이면
    print("경로 우대: 무료 입장입니다!")
    price = 0
elif age >= 13:                            # 그게 아니고, 13세 이상이면
    print("성인 요금입니다.")
    price = 30000
elif age >= 3:                             # 그게 아니고, 3세 이상이면
    print("어린이 요금입니다.")
    price = 15000
else:                                      # 위 조건이 모두 아니면 (3세 미만)
    print("영유아: 무료 입장입니다!")
    price = 0

print(f"결제 금액: {price:,}원")
```
### 반복문
> for문
- `for`문의 기본 사용법
- `range()` 함수로 숫자 범위 만들기
- `enumerate()`, `zip()` (심화)

- 사용 예제
```
# ✅ 반복문을 사용하면!
scores = [85, 90, 78, 92, 88]  # 점수들을 리스트에 담아요
total = 0                       # 합계를 저장할 변수

for score in scores:            # scores에서 점수를 하나씩 꺼내서
    total += score              # 합계에 더해요

average = total / len(scores)   # 합계 ÷ 학생 수 = 평균
print(f"평균: {average}")

# 🎉 학생이 100명이어도 코드는 똑같아요!
```
- 사용예제2
```
# 과일 리스트를 만들어요
fruits = ["사과", "바나나", "오렌지"]

# 리스트에서 과일을 하나씩 꺼내서 출력해요
for fruit in fruits:
    print(f"과일: {fruit}")

# 출력 결과:
# 과일: 사과
# 과일: 바나나
# 과일: 오렌지
```
- range() 함수: 숫자 범위 만들기
```
# range(5) = 0, 1, 2, 3, 4 (5개의 숫자를 만들어요)
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4
```
- zip() - 여러 리스트를 짝 지어서 처리
```
# 세 개의 리스트가 있어요
names = ["철수", "영희", "민수"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

# zip으로 세 리스트를 짝 지어요 (지퍼처럼!)
for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score}점 ({grade}등급)")

# 출력
# 철수: 85점 (B등급)
# 영희: 92점 (A등급)
# 민수: 78점 (C등급)
```
> While문
- `while`문의 기본 사용법
- `for`와 `while`은 언제 쓰는지
- 무한 루프와 탈출 방법
- 사용예제
```
count = 0                    # 카운터를 0으로 시작

while count < 5:             # count가 5보다 작은 동안 반복
    print(f"count: {count}")
    count += 1               # ⚠️ 이 줄이 없으면 무한 루프!

print("반복 종료!")
```
## 함수
- 반복되는 상황을 복잡하지 않게 한번에 선언하는 방법!!!
- 사용 예시
```
# 함수 정의 (만들기)
def 함수이름(매개변수1, 매개변수2):
    """독스트링: 함수 설명 (선택사항이지만 권장!)"""
    # 실행할 코드
    return 반환값  # 결과 돌려주기 (선택사항)

# 함수 호출 (사용하기)
결과 = 함수이름(인자1, 인자2)
```

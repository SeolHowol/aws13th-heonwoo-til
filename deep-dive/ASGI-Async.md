#  ASGI와 비동기(Async) 처리

## 1. Introduction: ASGI와 Async가 필요한가?
### 기존 웹 서버 방식의 한계
1. 동기처리란?
   1. **정의**: [초창기 방식] 클라이언트가 서버에 Request을 보내면, 서버의 Response가 도착할 때까지 클라이언트가 다른 작업을 하지 않고 **대기(Blocking)** 하는 방식
   2. **데이터 일관성**: 요청에 대한 즉각적인 결과를 받으므로 데이터의 최신 상태를 보장
   3. **구현 단순성**: 작업 순서를 제어하기 쉽고 설계가 단순
2. 동기처리의 문제점?
   1. **블로킹(Blocking) 발생**: 요청을 보낸 서버는 응답을 받을 때까지 메모리 등 자원을 점유한 채 대기
   2. **응답 대기 시간 증가**: 작업이 완료될 때까지 다른 작업을 수행할 수 없어 전체적인 처리량(Throughput)이 감소
   3. **병렬 처리의 어려움**: 하나의 요청이 완료되어야 다음 작업을 할 수 있어, 대규모 트래픽이 몰릴 때 개별 서비스를 독립적으로 확장이 어려움
## 2. 동기 vs. 비동기 
### 2.1 동기처리 방식
1. [Blocking] 동기 처리란 하나의 작업이 끝날 때까지 다음 작업을 수행하지 않는 방식
   - **$\color{#FF0000} 요청 → 처리 완료 → 다음 요청$**
   - 현재 작업이 끝나기 전까지 프로그램이 멈춰 있는 상태
2. **Blocking** 이란?
   - 프로그램의 실행 흐름이 대기 상태에 묶이는 것
   - Blocking I/O란? $\color{#0000FF} (JEFF의 힌트)$
     - 입출력(I/O) 작업이 끝날 때까지 프로그램(스레드)이 멈춰서 기다리는 방식
     - **고성능 서버, 실시간 서비스에 부적절**
### 2.2 비동기처리 방식
1. 비동기 처리는 어떤 작업의 완료를 기다리지 않고 다음 작업을 수행하는 방식
   - **$\color{#FF0000} 요청 → 대기 상태로 등록 → 다른 작업 수행 → 완료 시 결과 처리 $**
   - **기다리는 동안 다른 일을 병렬 처리**
2. Non-blocking
   - 작업을 시작만 하고 완료 여부는 나중에 확인
   - 실행 흐름이 멈추지 않음
3. Event Loop $\color{#0000FF} (JEFF의 힌트)$
   - 호출 스택이 비었을 때 태스크 큐(콜백 큐)에 있는 함수를 호출 스택으로 옮겨 실행시키는 무한 반복 과정
### 2.3 동기(Sync) vs 비동기(Async) 비교
| 구분    | 동기(Sync) | 비동기(Async)   |
| ----- | -------- | ------------ |
| 실행 방식 | 순차적    | 병렬적/독립적    |
| 대기 방식 | Blocking | Non-blocking |
| 요청 처리 | 하나씩 처리   | 여러 작업 동시 처리  |
| 자원 활용 | 비효율적     | 효율적          |
## 3. WSGI vs ASGI
> Python 웹 프레임워크의 성능과 처리 방식의 차이는 버와 애플리케이션이 요청을 어떻게 주고받는가라는 구조적인 차이에서 발생
### 3.1 WSGI(Web Server Gateway Interface)란?
1. Python 웹 서버와 웹 애플리케이션 간의 통신을 정의한 기존 표준 인터페이스
   - Django, Flask와 같은 초기 웹 프레임워크들이 기본적으로 채택
   - 웹 서버(Gunicorn, uWSGI 등)와 애플리케이션 사이의 연결 규칙을 정의
2. WSGI의 특징
   - 동기 기반 처리
   - 요청이 끝나야 다음 요청을 처리할 수 있음
### 3.2 WSGI의 한계점
   - 동시 처리 성능의 한계
   - 실시간 서비스에 취약
   - 서버 자원 낭비
### 3.3 ASGI(Asynchronous Server Gateway Interface)란?
1. WSGI의 한계를 해결하기 위해 등장한 비동기 서버 인터페이스 표준
   - Python에서 비동기 프로그래밍을 본격적으로 활용 가능
   - FastAPI, Starlette 등이 ASGI 기반으로 설계
## 4. ASGI 동작 구조 
> 요청을 처리하는 전체 구조가 이벤트 중심(Event-driven)으로 설계
### 4.1 ASGI 아키텍처 흐름
> Client → ASGI Server → Application → Response
1. Client
   - 웹 브라우저, 모바일 앱, API 클라이언트
2. ASGI Server (Uvicorn)
   - 클라이언트 요청 수신
   - Event Loop 관리 요청을
   - ASGI 애플리케이션으로 전달
3. Application (FastAPI)
   - 실제 비즈니스 로직을 처리
   - async def 함수 기반으로 요청 처리
   - 필요 시 I/O 작업(DB, 외부 API 등)을 비동기적으로 수행
4. Response
   - 처리 결과를 다시 ASGI Server로 반환
   - ASGI Server가 클라이언트에게 응답 전송
### 4.2 ASGI 아키텍처의 핵심 구성 요소
1. Event Loop **(관제탑)**
   - 모든 작업을 관리하는 중심 시스템
   - 여러 요청을 하나의 루프에서 관리
   - 작업 간 전환(Context Switching)을 효율적으로 수행
2. Coroutine **(세이브 포인트)**
   - 중단 및 재개가 가능한 함수
   - `async def` 로 정의
   - `await` 지점에서 실행을 멈췄다가 다시 이어서 실행
3. Non-blocking I/O **(딴짓)**
   - I/O 작업이 끝날 때까지 프로그램을 멈추지 않음
   - 대기 시간 동안 다른 요청 처리 가능
### 4.3 Blocking 코드 vs Non-blocking 코드
> ASGI 구조에서도 Blocking 코드가 Event Loop를 멈추게 만들기 때문에 주의
1. Blocking code
```
import time

async def blocking_task():
    time.sleep(3)
    return "done"
```
   - time.sleep(3)은 동기 함수
     - Event Loop 전체가 멈춤
     - 다른 요청 처리 불가
2. Non-blocking code
```
import asyncio

async def non_blocking_task():
    await asyncio.sleep(3)
    return "done"
```
   - await asyncio.sleep(3)은 동기 함수
     - Event Loop에 제어권 반환
     - 다른 요청 처리 가능
## 5. FastAPI의 ASGI를 활용 방법
> FastAPI는 단순히 “Python으로 만든 웹 프레임워크”가 아니라,
ASGI 기반 비동기 처리 구조를 전제로 설계된 프레임워크

> ASGI와 async / await가 활용
### 5.1 FastAPI 개요
> FastAPI는 **Python 3.7** 이상에서 동작하는 현대적인 웹 프레임워크로, ASGI 표준을 기반으로 설계 

- FastAPI는 기존 프레임워크와 다음과 같은 차별점

| 항목       | 기존(Django / Flask) | FastAPI    |
| -------- | -------------- | ---------- |
| 기본 처리 방식 | 동기(Sync)       | 비동기(Async) |
| 서버 표준    | WSGI           | ASGI       |
| async 지원 | 제한적            | 기본 설계      |
| 동시 요청 처리 | 낮음             | 매우 높음      |
| 실시간 기능   | 구현 복잡          | 자연스럽게 지원   |

### 5.2 `async / await`의 실제 의미
1. `async def`의 의미
   - **필요할 때 실행을 멈출 수 있는 함수**
   - `async def`로 정의된 함수는 Coroutine 함수
   - 실행 중 중단(suspend) 과 재개(resume) 가 가능
   - Event Loop에 의해 관리됨
```
async def get_data():
    ...
```
2. `await`의 의미
   - **CPU를 다른 작업에게 넘기는 지점**
   - “이 작업이 끝날 때까지 나는 잠시 멈출 테니 Event Loop에게 제어권을 돌려준다”
   - 다른 요청 처리
   - 다른 Coroutine 실행
```
result = await fetch_from_db()
```
### 5.3 FastAPI가 빠르다?
1. 같은 Python 코드라면 연산 속도는 거의 동일
2. 대기 시간을 효율적으로 활용

## 6. ASGI 서버: Uvicorn의 역할
### 6.1 Uvicorn이란?
> Uvicorn은 Python으로 작성된 **ASGI 서버**로, ASGI 표준을 따르는 애플리케이션(FastAPI 등)을 실행하는 역할

1. Uvicorn의 기본 역할
   - 클라이언트로부터 요청
   - 수신 HTTP / WebSocket 프로토콜 처리
   - Event Loop 실행 및 관리
   - ASGI 애플리케이션(FastAPI) 호출
   - 처리 결과를 클라이언트에게 응답
2. Event Loop 기반 서버
   - Uvicorn은 내부적으로 Event Loop 를 사용하여 동작

## 7. (제일 중요!!!!!) 그럼 비동기 처리가 무조건 좋을까? 그리고 주의사항은 없을까?
### 7.1 비동기 처리 문제점 (CPU 연산이 많은 작업)
> 비동기 처리는 연산을 빠르게 하는 것이 아닌 효율적으로 하는 것!!!

1. 비동기 처리에 적합하지 않은 작업 (GPU 연산이 많은 작업)
   - 대규모 수학 계산
   - 이미지/영상 처리 암호화
   - 머신러닝 추론
2. GPU 연산이 많은 작업이 비동기 처리에 적합하지 않은 이유
   - CPU를 지속적으로 사용
   - 중간에 대기가 거의 없음
   - Event Loop에 제어권을 넘길 지점이 없음

### 7.2 Blocking 라이브러리 
> Blocking 라이브러리를 무심코 사용

1. Blocking 사용시 문제점
   - 동시 처리 수 급감
   - 응답 시간 증가
   - 트래픽 증가 시 서버 다운 위험

### 7.3 언제 비동기가 효과적인가?
1. 데이터베이스 접근
   - SELECT, INSERT, UPDATE
   - 디스크 및 네트워크 대기 발생
2. 외부 API 호출
   - 결제 API
   - 인증 서버
   - 외부 데이터 수집
3. 파일 및 네트워크 작업
   - 파일 업로드/다운로드
   - 로그 저장
   - 클라우드 스토리지 접근

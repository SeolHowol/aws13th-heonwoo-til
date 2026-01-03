import sqlite3

# DB 연결
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 테이블 예시 (없으면 한 번만 실행)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    age INTEGER
)
""")

# 사용자 입력
name = input("이름: ")
age = int(input("나이: "))

# ✅ 안전한 파라미터 바인딩
sql = "INSERT INTO students (name, age) VALUES (?, ?)"
cursor.execute(sql, (name, age))

conn.commit()
conn.close()
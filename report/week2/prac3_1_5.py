#제공하는 기본 함수
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}

# 최고값을 찾기 위한 변수
max_score = 0
max_name = ""

# for 문을 통해 최고값과 현재값을 비교하고 더 큰 값을 저장
for name, score in scores.items():
    if score > max_score:
        max_score = score
        max_name = name

print(f"maximum score is {max_score}, and best score name is {max_name}")
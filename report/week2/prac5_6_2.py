str_numbers = ["10", "20", "30", "40", "50"]

# 1단계: 정수로 변환
# 2단계: 100 더하기
result = list(map(lambda x: int(x)+100, str_numbers))

print(result)

# 결과: [110, 120, 130, 140, 150]
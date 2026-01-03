# 점수 입력
score = int(input("Write your score here: "))

#추가 조건 0 ~ 100 범위 외에는 잘못된 입력임을 알리기
while (score > 100) or (score < 0):
    print("\nWrite your score between 0 and 100")
    score = int(input("Write your score here: "))


# 성적 분류
if score >= 90:
    print("You got a A grade")
elif score >= 80:
    print("You got a B grade")
elif score >= 70:
    print("You got a C grade")
elif score >= 60:
    print("You got a D grade")
else:
    print("You got a F grade")
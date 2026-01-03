import random

# 게임 시작 문구
print("\n----Welcome to number baseball game world!----\n")

# 게임 숫자 범위 설정 안내
range_num = int(input("Please specify the range of numbers to be used in the game: "))

# 정답값 및 플레이어 답변
real_answer = random.randint(1, range_num)  # 1~100 사이 랜덤 정수
player_answer = 0

# 플레이어가 답변한 횟수
count = 0

# 정답이 나올때까지 반복
while real_answer != player_answer:
    player_answer = int(input("Please enter your guess: "))
    count += 1                           # 반복횟수 확인
    if player_answer > real_answer:
        print("Your guess is too high!")
    elif player_answer < real_answer:
        print("Your guess is too low!")

print(f"Your guess is correct! You guessed {count} times!")

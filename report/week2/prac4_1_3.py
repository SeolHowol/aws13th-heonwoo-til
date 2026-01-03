# 원하는 숫자 입력
goal_num = int(input("How many numbers do you want? "))

# prime number list
prime_num = []

# 2부터 원하는 숫자까지 반복하여 소수인지 판별
for num in range(2, goal_num):
    prime_num.append(num)  # 소수라고 가정 그냥 했을 때, 2를 인식하지 못 함
    for j in range(2, num):
        if  j == num-1:    # 자신을 제외한 숫자까지 나누어 떨어지지 않는 경우 for 문 탈추
            break
        elif num % j == 0: # 나누어 떨어지는 경우 소수 리스트에서 제외
            prime_num.remove(num)
            break

# 리스트 출력 (for 문을 이용하지 않는 경우 괄호도 함께 출력)
for i in prime_num:
    print(i, end=" ")
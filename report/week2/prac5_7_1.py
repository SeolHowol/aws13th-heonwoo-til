def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b
    else:
        return "지원하지 않는 연산자입니다."

print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # 0으로 나눌 수 없습니다
print(calculator(10, 5, '%'))  # 지원하지 않는 연산자입니다

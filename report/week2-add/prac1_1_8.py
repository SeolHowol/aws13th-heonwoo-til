def is_float(s):
    try:
        float(s)  # 문자열을 float으로 변환 시도
        return True
    except ValueError:
        return False

while True: # 숫자의 정상 입력 확인
    num1 = str(input("first number: "))
    operator = input("operator: (+, -, *, /, //, %): ")
    num2 = str(input("second number: "))
    if is_float(num1) and is_float(num2) :
        pass
    else:
        print("\n올바른 숫자를 입력해주세요")
        continue


    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        result = num1 + num2
        break
    elif operator == "-":
        result = num1 - num2
        break
    elif operator == "*":
        result = num1 * num2
        break
    elif operator == "/":
        if num2 == 0:
            print("\nerror: the number to divide by zero!")
        else:
            result = num1 / num2
            break
    elif operator == "//":
        result = num1 // num2
        break
    elif operator == "%":
        result = num1 % num2
        break
    else:
        print("\nerror: the operator '%s' is not supported" % operator)


print(f"\nresult {num1} {operator} {num2} = {result}")

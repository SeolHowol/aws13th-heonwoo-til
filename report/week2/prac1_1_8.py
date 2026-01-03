num1 = float(input("first number: "))
operator = input("operator: (+, -, *, /, //, %): ")
num2 = float(input("second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("error: the number to divide by zero!")
    else:
        result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
else:
    print("error: the operator '%s' is not supported" % operator)
    result = None

if result is not None:
    print(f"\nresult {num1} {operator} {num2} = {result}")
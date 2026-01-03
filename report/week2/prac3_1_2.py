password = input("write your password: ")

if len(password) < 8:
    print("password is too short")
else:
    print("password is good!")
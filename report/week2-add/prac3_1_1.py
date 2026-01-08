email = input("Enter your email: " )
if "@" in email and email.count("@") == 1:
    separate_email = email.split("@")
    print("사용자 이름:" + separate_email[0])
    print("도메인:" + separate_email[1])
else:
    print("올바른 이메일 형식이 아닙니다.")
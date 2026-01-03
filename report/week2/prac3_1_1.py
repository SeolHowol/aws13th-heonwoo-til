email = input("Enter your email: " )
separate_email = email.split("@")

print("사용자 이름:" + separate_email[0])
print("도메인:" + separate_email[1])
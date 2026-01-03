def validate_password(password):
    digit_TF = False
    size_TF = False

    if len(password) < 8:
        return False,"8자 이상이어야 합니다."
    for char in password:
        if char.isdigit():
            digit_TF = True
        if char.isupper():
            size_TF = True

    if not digit_TF:
        return False, "숫자를 포함해야 합니다."
    elif not size_TF:
        return False, "대문자를 포함해야 합니다."

    return True, "유효한 비밀번호 입니다."



print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")
# 제공하는 기초자료
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]

# 리스트 형 -> 세트 형으로 변경
# 순서에 제한 없이 비교를 위해서 순서가 없는 세트 형을 활용
set_chul = set(chulsoo)
set_young = set(younghee)

# &를 통해서 set형의 공통 변수 도출 가능
common = set_chul & set_young

# f를 통해 여러 형의 변수가 포함된 문자열을 출력
print(f"공통: {common}")
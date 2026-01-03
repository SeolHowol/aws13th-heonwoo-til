def print_report(name, scores):

    # 성적 분석 계산
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    # 성적 분석 출력부
    print(f"=== {name} 성적표 ===")
    print(f"점수: {scores}점")
    print(f"평균: {average}점")
    print(f"최고점: {max_score}점")
    print(f"최저점: {min_score}점")

    # 최종 성적 평가
    if average > 90:
        print("등급: A")
    elif average > 80:
        print("등급: B")
    elif average > 70:
        print("등급: C")
    elif average > 60:
        print("등급: D")
    else:
        print("등급: F")


print_report("김철수", [85, 92, 78, 96, 88])
# 예상 출력:
# === 김철수 성적표 ===
# 점수: [85, 92, 78, 96, 88]
# 평균: 87.8점
# 최고점: 96점
# 최저점: 78점
# 등급: B
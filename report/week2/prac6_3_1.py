class Student:
    def __init__(school,name , student_id, grade):
        school.name = name
        school.student_id = student_id
        school.grade = grade
    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다. (학번: {self.student_id})")

kim = Student("김철수", "2024001", 1)
kim.introduce()

# 출력: 안녕하세요, 1학년 김철수입니다. (학번: 2024001)
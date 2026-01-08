class Student:
    def __init__(self,name , student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다. (학번: {self.student_id})")

kim = Student("김철수", "2024001", 1)
kim.introduce()
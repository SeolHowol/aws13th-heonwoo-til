import csv

students = [
    {'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
    {'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
    {'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['학번', '이름', '학과']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
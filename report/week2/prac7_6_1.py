import csv

with open('users.csv', 'r', encoding='utf-8') as file:
    reading = csv.DictReader(file)
    for row in reading:
        print(f"{row['이름']} - {row['직업']}")
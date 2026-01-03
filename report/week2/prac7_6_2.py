import csv

with open('users.csv', 'r', encoding='utf-8') as file:
    reading = csv.DictReader(file)
    for row in reading:
        age = int(row['나이'])
        if age > 29:
            print(f"{row['이름']}({row['나이']}세)")

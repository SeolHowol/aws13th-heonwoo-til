import csv
import json

# CSV 읽기
with open('users.csv', 'r', encoding='utf-8') as f:
    users = list(csv.DictReader(f))

# JSON 쓰기
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
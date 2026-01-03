import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

print(f"앱 이름: {config['app_name']}")
print(f"버전: {config['version']}")
print(f"DB 호스트: {config['database']['host']}")
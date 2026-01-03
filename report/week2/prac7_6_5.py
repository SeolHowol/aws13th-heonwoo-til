import json

# 읽기
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 수정
config['debug'] = True
config['features'].append('notifications')

# 저장
with open('config_updated.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

# 할인율 20% 이상만 추출
discounted = filter(lambda x: x["discount"] > 20, products)
print(list(discounted))
# 결과: [{'name': '마우스', 'discount': 25}, {'name': '키보드', 'discount': 30}]
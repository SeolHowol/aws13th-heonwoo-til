cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

# 인구수 오름차순 정렬
sorted_cities = sorted(cities, key=lambda x: x["population"])

for city in sorted_cities:
    print(city["name"], end=" ")

# 원하는 구구단 단위
gugudan = int(input("\nplease enter a number for gugudan: "))

# 구구단 출력
print(f"\n==={gugudan}단===")
for i in range(1, 10):
    print(f"{gugudan} x {i} = {i * gugudan}")
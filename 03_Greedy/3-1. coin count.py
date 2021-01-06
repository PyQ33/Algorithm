n = 1260
count = 0
result = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count = n // coin  # 해당 coin 화폐로 거슬러 줄수 있는 동전 수 세기
    result += count
    print(f"{coin}:: {count} 개")
    print(f"+ {coin * count} 원")
    n = n % coin
print(result)
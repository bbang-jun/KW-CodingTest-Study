n = int(input())
house = list(map(int, input().split()))
house.sort()

if len(house) % 2 == 0:
    # 짝수
    idx = len(house) // 2
    result = house[idx-1]
else:
    # 홀수
    idx = len(house) // 2
    result = house[idx]
print(result)
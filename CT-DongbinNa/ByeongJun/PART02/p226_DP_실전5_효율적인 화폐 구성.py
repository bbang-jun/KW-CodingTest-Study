N, M = map(int, input().split())

money = []
dp_table = [10001] * (M+1)

for _ in range(N):
    money.append(int(input()))

dp_table[0] = 0 # 0원은 방법이 없으므로 0

for i in range(N):
    for j in range(money[i], M+1):
        if dp_table[j-money[i]] != 10001:
            dp_table[j] = min(dp_table[j], dp_table[j - money[i]] + 1)

if dp_table[M] == 10001:
    print(-1)
else:
    print(dp_table[M])

# 답지 참조
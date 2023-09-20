n,m=map(int,input().split())
dp = [10001] * (m+1)
money = []

for _ in range(n):
    money.append(int(input()))

for i in range(n):
    for j in range(money[j], m+1):
        if dp[j- money[i]] != 0:
            dp[j] = min(dp[j], dp[j-money[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

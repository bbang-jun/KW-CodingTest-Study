n=int(input()) # 100개 최대
food = list(map(int,input().split())) # 각 1000개까지 최대

dp = [0]* 101
dp[1] = food[0]
dp[2] = max(food[0], food[1]) #누적합

for i in range(3,n+1): # O(n)
    dp[i] = max(dp[i-2]+food[i-1], dp[i-1])
    # 지금까지 전에 누적된 합이랑, 두칸 전 + 현재 food값 누적 중 큰 값 선택
print(dp[n])

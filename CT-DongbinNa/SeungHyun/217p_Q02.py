X = int(input())

# dp 테이블 초기화
dp = [0] * 30001

# dp (dp[0], dp[1] 모두 0이기 때문에 2부터 for loop를 시작)
for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    # 각각 X를 5, 3, 2로 나눠주는 경우
    # 큰 수로 나눠줘야 더 빨리 감소하므로 5, 3, 2 순으로 배치
    if(i % 5 == 0): dp[i] = min(dp[i], dp[i//5]+1)
    if(i % 3 == 0): dp[i] = min(dp[i], dp[i//3]+1)
    if(i % 2 == 0): dp[i] = min(dp[i], dp[i//2]+1)
    
print(dp[i])
x=int(input())
dp = [0]*(30001)

for i in range(2,30001):
    # bottom-up, dp 테이블 사용

    dp[i] = dp[i-1]+1 #최소한의 연산 +1

    # 문제를 푸는 작은경우의수 3개
    # O(n) 입력개수가 n일때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i//5]+1)

print(dp[x])

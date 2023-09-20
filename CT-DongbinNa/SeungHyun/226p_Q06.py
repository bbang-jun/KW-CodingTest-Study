# unsolved(책 풀이 참고)
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

array = []
for i in range(N):
    array.append(int(input()))

dp = [10001] * (M+1)

dp[0] = 0
for i in range(N):
    for j in range(array[i], M+1):
        if dp[j-array[i]] != 10001:
            dp[j] = min(dp[j], dp[j-array[i]]+1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
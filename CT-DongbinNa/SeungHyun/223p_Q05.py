import sys

# 입력
N = int(input())

# 결과를 저장하기 위한 배열
dp = [0] * 1002

# 제일 큰 타일이 2*2이므로 가로가 2인 경우까지는 고정
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796
    
print(dp[N])
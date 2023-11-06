n=int(input())
dp = [0] * 1001
dp[1], dp[2] = 1,3

for i in range(3,1001): #O(n)
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796
    #순서를 바꾸는 경우는 x, 왼쪽부터 채워나감
print(dp[n])

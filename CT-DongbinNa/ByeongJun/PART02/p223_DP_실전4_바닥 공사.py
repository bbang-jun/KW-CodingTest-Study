N = int(input())

dp_table = [0] * 1000

for i in range(1, N+1):
    if i == 1:
        dp_table[1] = 1
    elif i == 2:
        dp_table[2] = 3
    else:
        dp_table[i] = (dp_table[i-1] + 2*dp_table[i-2]) %796796

print(dp_table[N])

# 의문: i-2를 채우는 경우에서 1x2 2개로 채우는 경우, 2x1 2개로 채우는 경우, 2x2 1로 채우는 경우까지 총 3가지 경우가 아닌 이유
# 3*dp_table[i-2]
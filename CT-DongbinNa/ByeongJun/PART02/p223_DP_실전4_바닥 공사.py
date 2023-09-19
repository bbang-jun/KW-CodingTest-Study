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
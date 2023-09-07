N,M = map(int,input().split())
res = 0
for _ in range(N):
    row = list(map(int,input().split()))
    row.sort(reverse=True)

    if row[-1] > res: #더작은게 있으면 갱신
        res = row[-1]
print(res)

N, M = map(int, input().split())

data = []
Results = []

for _ in range(N):
    row = list(map(int,input().split()))
    data.append(row)

for i in range(N):
    Min = 10001
    for j in range(M):
        if data[i][j] < Min:
            Min = data[i][j]
    Results.append(Min)

Results.sort()
print(Results[N-1])
N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
Result = 0

for i in range(M):
    if i % K == 0 and i != 0:
        Result += data[N-2]
        continue

    Result += data[N-1]

print(Result)
N, K = map(int, input().split())

times = 0

while True:
    if N == 1:
        break
    if N % K == 0:
        N /= K
    else:
        N -= 1
    times += 1

print(times)
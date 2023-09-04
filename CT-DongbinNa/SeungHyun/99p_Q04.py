N, K = map(int, input().split())

result = 0

while True:
    if N//K > 0:
        if N % K == 0:
            result += 1
            N //= K
        else:
            result += 1
            N -= 1
    else: break

if N != 1:
    result += (N-1)

print(result)
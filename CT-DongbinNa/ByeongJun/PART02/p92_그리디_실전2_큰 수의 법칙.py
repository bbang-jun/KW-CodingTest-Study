N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True) # 크기 내림차순 정렬

result = 0
i = 0

for _ in range(M):
    if i >= K:
        result += numbers[1]
        i = 0
    else:
        result += numbers[0]
        i += 1

print(result)
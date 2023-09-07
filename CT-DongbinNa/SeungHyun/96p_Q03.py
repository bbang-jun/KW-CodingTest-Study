# N: 행의 개수, M: 열의 개수
N, M = map(int, input().split())

result = 0

for i in range(N):
    num_list = list(map(int, input().split()))
    num_list.sort()
    minimum = num_list[0]
    result = max(result, minimum)

print(result)
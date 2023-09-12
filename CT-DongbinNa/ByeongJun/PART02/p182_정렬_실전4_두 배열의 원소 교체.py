N, K = map(int, input().split())

result = 0

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort() # 1 2 3 4 5
array_b.sort(reverse=True) # 6 6 5 5 5

for i in range(K):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]

for a in array_a:
    result += a

print(result)
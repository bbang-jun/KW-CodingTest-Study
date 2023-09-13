N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

for value in array:
    print(value, end=" ")
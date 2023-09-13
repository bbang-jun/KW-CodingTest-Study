N = int(input())

Arr = []
for _ in range(N):
    Arr.append(int(input()))

#sort by descending order
Arr.sort(reverse=True)
print(Arr)
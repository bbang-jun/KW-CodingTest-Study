N=int(input())
li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)
print(*li)

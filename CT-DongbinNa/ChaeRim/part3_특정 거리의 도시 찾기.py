import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
dis = [-1] * (n+1)
dq = deque([x])
dis[x] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

while dq:
    start = dq.popleft()

    for nx in graph[start]:
        if dis[nx] == -1:
            dis[nx] = dis[start] +1
            dq.append(nx)

flag = False
for i in range(1,n+1):
    if dis[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)

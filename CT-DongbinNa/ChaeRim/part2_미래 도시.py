import sys
input = sys.stdin.readline

INF = int(1e9) #무한 10억
n,m = map(int,input().split()) #노드, 간선
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j: graph[i][j] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1 # 두회사 사이 비용은 1
    graph[b][a] = 1

x,k = map(int,input().split()) # k를 거쳐 x로 감

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

if graph[1][k] + graph[k][x] >= INF:
    print('-1')
else:
    print(graph[1][k] + graph[k][x])

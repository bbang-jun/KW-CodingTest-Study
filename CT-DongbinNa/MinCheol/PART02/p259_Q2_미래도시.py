#Starts with 1 and visit K to X
import heapq
INFINITE = int(1e9)

N, M = map(int,input().split())
#initialize distance between spot
graph = [[INFINITE] * (N+1) for _ in range(N+1) ]
for i in range(N+1):
    for j in range(N+1):
        if i==j:
            graph[i][j]==0

#initialize distance
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B]=1
    graph[B][A]=1


for K in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][K] + graph[K][b])
            graph[b][a] = min(graph[b][a], graph[b][K] + graph[K][a])

X, K = map(int, input().split())

if graph[1][K]==INFINITE or graph[K][X]==INFINITE:
    print(-1)
else:
    print(graph[1][K]+graph[K][X])

#I think it have to think about not only [a][b] but also [b][a]
#the solution have some problem
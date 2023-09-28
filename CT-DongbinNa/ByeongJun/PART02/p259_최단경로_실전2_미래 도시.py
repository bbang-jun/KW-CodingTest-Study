INF = int(1e9)

N, M = map(int, input().split()) # N = 회사의 개수, M = 경로의 개수
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a==b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split()) # X = 최종 회사, K = 소개팅 회사

result = -1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if a==1 and k==K and b==X: # 시작이 1, 거쳐가는 k, 도착하는 b
                result = graph[a][k] + graph[k][b]

if result >= INF:
    print(-1)
else:
    print(result)
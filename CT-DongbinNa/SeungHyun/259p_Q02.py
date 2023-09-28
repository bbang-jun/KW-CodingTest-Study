import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 및 간선의 개수 입력 받기
N, M = map(int, input().split())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# X: 판매, K: 소개팅
X, K = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for K in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            # a에서 b로 이동할 때 아래 두 가지 경우를 늘 계산해야 함
            # 1. 직접 가는것이 빠른지
            # 2. K를 거쳐서 가는 것이 빠른지
            graph[a][b] = min(graph[a][b], graph[a][K] + graph[K][b])

# 문제의 조건에 따라 시점: 1, 종점: X, 반드시 거쳐야 하는 점: K 
if(graph[1][K] + graph[K][X] >= INF):
    print("-1")
else:
    print(graph[1][K] + graph[K][X])

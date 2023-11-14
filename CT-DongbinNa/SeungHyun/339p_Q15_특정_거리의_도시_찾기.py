import sys
input = sys.stdin.readline

from collections import deque

# 도시의 정보 입력
n, m, k, x = map(int, input().split())
# 그래프 초기화
graph = [[] for _ in range(n + 1)]
# 거리의 정보는 -1로 초기화
distance = [-1] * (n + 1)
result = []

# 도시의 연결 정보를 그래프 리스트에 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발 도시 -> 출발 도시의 거리는 0 (BFS 시작)
distance[x] = 0
q = deque([x])

while q:
    # 그래프에 저장된 도시의 연결정보를 불러와서 
    # 도시 하나씩 차례대로 연결된 모든 도시를 탐색해서 최단 거리를 +1
    now = q.popleft()
    for nextNode in graph[now]:
        if distance[nextNode] == -1:
            distance[nextNode] = distance[now] + 1
            q.append(nextNode)
            # 최단 거리가 K가 되면 result 리스트에 도시 번호를 저장
            if distance[nextNode] == k:
                result.append(nextNode)

if not result:
    print(-1)
else: # 오름차순 출력
    result.sort()
    for city in result:
        print(city)

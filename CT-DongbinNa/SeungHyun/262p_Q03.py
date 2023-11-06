import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 나타내는 값(10억)


def dijkstra(start):
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N, M, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(N+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

# 모든 정보를 입력받기
for _ in range(M):
    # X 도시에서 Y 도시로 전달되는 시간이 Z
    X, Y, Z = map(int, input().split())
    graph[X].append((Y,Z))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 각각 도시의 수, 가장 멀리 있는 도시와의 최단 거리
result = 0
min_distance = 0

for d in distance:
    if d == INF:
        continue
    else:
        result += 1
        min_distance = max(min_distance, d)

print(result-1, min_distance)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

start = C
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 자기 자신으로 가는 비용은 0
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

total_city = 0
total_time = 0

for i in range(1, N + 1):
    if distance[i] == INF or i == start:
        continue
    total_time = max(total_time, distance[i])
    total_city += 1

print(f"{total_city} {total_time}")

# 모두 메시지를 받는다는 것의 의미가 총 걸리는 시간이 아니라 마지막에 받은 시간을 의미함.
# 모두 보내게되는.. 최단시간, 범위가 크다 -> 다익스트라
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    x,y,cost = map(int,input().split())
    graph[x].append((y,cost))

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        # (거리, 현재노드) 꺼내기
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 짧은 거리 갱신
                heapq.heappush(hq,(cost,i[0]))
dijkstra(c)
cnt, time = 0,0
for i in range(1,n+1):
    if distance[i] != INF:
        cnt += 1
        time = max(distance[i],time)

# 개수는 시작노드 제외 출력
print(cnt-1, time)

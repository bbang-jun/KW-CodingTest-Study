#N is number of city
#M is number of connection
#C is city of emergency
#X is from Y is to, Z is cost(time)
#Get the maximum time to reach imergency message

import heapq
INFINITE = int(1e9)

N, M, C = map(int,input().split())

#initialize distacne and graph
Distance = [INFINITE]*(N+1)
graph = [[] * (N+1) for _ in range(N+1)]

#initialize Graph
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def Dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    Distance[start]=0
    while q:
        Dist, Now = heapq.heappop(q)
        for i in graph[Now]:
            Cost = Dist + i[1]
            if Cost < Distance[i[0]]:
                Distance[i[0]] = Cost
                heapq.heappush(q, (Cost, i[0]))

Dijkstra(C)

Count = 0
Max = 0
for i in range (N+1):
    if Distance[i]!=INFINITE and i!=C: Count+=1; Max= max(Max, Distance[i])
print(Count, Max)

#same as Example
# 길은 어느 방향이로든지 다닐 수 있다 = 양방향
# N개의 집과 집들을 연결하는 M개의 길 = 그래프 이론
# 두 집 사이의 경로가 존재하면서 길을 없앨 수 있다 & 유지비의 합을 최소 = 크루스칼 최소 신장 트리 적용
# 우선 크루스칼을 적용하여 minimum spanning tree를 하나 구하고, 가장 cost가 큰 간선 제거 시 유지비를 최소로 하면서 2개로 분할 가능
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)
cost = 0
most_cost = 0
for i in range(1, N + 1):
    parent[i] = i

edges = []

for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

for edge in edges:
    C, A, B = edge
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        cost += C
        most_cost = C

cost -= most_cost

print(cost)
import sys
input = sys.stdin.readline

# 필요없는 길 없애고 유지비의 합을 최소로 하니 최소 신장 트리
# 크루스칼 알고리즘 사용

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent,a,b):
    a,b = find(parent,a), find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
answer, last_edge = 0,0
n,m = map(int,input().split()) # O(MlogM)
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,cost = map(int,input().split())
    # 비용 기준 정렬
    edges.append((cost,a,b))
edges.sort() #O(logN)

for i in edges:
    cost,a,b = i
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        answer += cost
        last_edge = cost # 하나 선 없앨거기에 마지막 비용 따로 저장

print(answer-last_edge)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#N is number of house
#M is number of street
N, M = map(int, input().split())

parent = [0]*(N+1)
Edges = []

for i in range(N+1):
    parent[i]=i

for _ in range(M):
    A, B, C = map(int, input().split())
    Edges.append((C,A,B))

Edges.sort()
result = 0
last = 0

for Edge in Edges:
    C, A, B = Edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        last = C

print(result-last)
#delete last cost of price

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4 
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
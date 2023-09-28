def Find_parent(parent, x):
    if parent[x] != x:
        parent[x] = Find_parent(parent, Parent[x])
    return parent[x]

def Union_Parent(parent, a, b):
    a = Find_parent(parent, a)
    b = Find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#N for number of student
#M for number of connection
N, M = map(int,input().split())

Parent = [0]*(N+1)

for i in range(N+1):
    Parent[i]=i

for _ in range (M):
    A, B, C = map(int,input().split())

    if A == 0:
        if Find_parent(Parent, B)==Find_parent(Parent, C):
            continue
        else:
            Union_Parent(Parent, B, C)
        
    else:
        if Find_parent(Parent, B)==Find_parent(Parent, C):
            print("YES")
        else:
            print("NO")

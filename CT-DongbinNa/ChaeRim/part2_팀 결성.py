import sys
input = sys.stdin.readline

# 특정원소 찾기
def find(partent,x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

# 두 원소가 속한 집합 합치기
def union(parent,a,b):
    a, b = find(parent,a), find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 팀 합치기, 같은 팀 확인 2가지 연산 -> 서로소 연산
n,m=map(int,input().split())
parent = [0]*(n+1) #부모 테이블 초기화

for i in range(1,n+1):
    parent[i] = i #자기 자신 초기화

for _ in range(m):
    select, a,b = map(int,input().split()) # 연산, a, b 입력
    if not select: # 팀 합치기
        union(parent,a,b)
    else:
        if find(parent,a) == find(parent,b): print('YES')
        else: print('NO')

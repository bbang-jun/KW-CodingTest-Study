# 서로소 집합 알고리즘 활용
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [0] * (N+1) # 부모 테이블 선언
# 부모 테이블 초기화(자기 자신으로)
for i in range(1, N+1):
    parent[i] = i

for i in range(M):
    type, a, b = map(int, input().split())

    if type == 0:
        union_parent(parent, a, b)
    elif type == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
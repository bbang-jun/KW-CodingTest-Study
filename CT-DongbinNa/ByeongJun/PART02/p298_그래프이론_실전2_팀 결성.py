# 0 a b: a 학생 팀과 b 학생 팀 union
# 1 a b: a 학생과 b 학생이 같은 팀인지 find
# 1 a b에 대해서 YES or NO 출력

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # parent 인자는 parent 리스트를 넘기기 위해, parent[x]는 root까지 가기 위한 현재 노드
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (M + 1)
results = []

for i in range(1, M + 1):
    parent[i] = i

for i in range(M):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union(parent, a, b)
    else:
        root_a = find(parent, a)
        root_b = find(parent, b)
        if root_a == root_b:
            results.append('YES')
        else:
            results.append('NO')

for result in results:
    print(result)
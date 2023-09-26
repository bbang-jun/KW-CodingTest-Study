import heapq
import sys
input = sys.stdin.readline

# 노드의 개수와 간선의 개수 입력
n, m = map(int, input().split())

# 부모 테이블 선언 및 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
# 유지비의 합이 최소인 경우: 유지비가 높은 경우를 제외하면 됨
maxCost = 0

# 부모 노드 찾는 함수
def getParent(num):
    if num == parent[num]:
        return num
    return getParent(parent[num])

# 두 노드를 합치는 함수
def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)

    if a != b:
        parent[a] = b

# 마을 간의 시점, 종점, 유지비를 입력 받는 동시에 정렬
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    # 두 노드의 부모가 같지 않다면 연결
    if (getParent(a) != getParent(b)):
        unionParent(a, b)
        result += cost
        maxCost = max(maxCost, cost)

print(result - maxCost)

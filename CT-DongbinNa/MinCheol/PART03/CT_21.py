from collections import deque
import math

MOVE= [(-1,0),(0,-1),(1,0),(0,1)]
N, L, R = map(int,input().split())

Arr = []
Temp = []
for i in range(N):
    Temp = list(map(int, input().split()))
    Arr.append(Temp)

print(Arr)

def bfs(i,j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    count = Arr[i][j]   # 총 연합된 국가 수 
        # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기 
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + MOVE[d][0]
            ny = y + MOVE[d][1]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny]:
                continue
            if L <= abs(Arr[nx][ny] - Arr[x][y]) <= R:
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += Arr[nx][ny]
    # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산  
    for x, y in union:
        Arr[x][y] = math.floor(count / len(union))

    return len(union)


Flag = True
Result = 0
while Flag:
    Flag=False
    visit = [[False] * N for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    Flag = True
    if not Flag:
        break
    Result += 1

print(Result)
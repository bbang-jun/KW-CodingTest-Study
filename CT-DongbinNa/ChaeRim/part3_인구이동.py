import sys
input = sys.stdin.readline
from collections import deque


N,L,R = map(int,input().split())
board = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(N):
    board.append(list(map(int,input().split())))

def checkVaild(i,j):
    return 0 <= i < N and 0 <= j < N

def bfs(i,j):
    dq = deque()
    dq.append((i,j))
    union = [(i,j)]

    while dq:
        y,x = dq.popleft()
        for i in range(4):
            ny = y+ dy[i]
            nx = x+ dx[i]
            if checkVaild(ny,nx) and not visited[ny][nx] and L <= abs(board[ny][nx] - board[y][x]) <= R:
                # 국경선 열어 연합에 추가
                union.append((ny,nx))
                visited[ny][nx] = True
                dq.append((ny,nx))
    return union

cnt = 0
while True:
    visited = [[False]*N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                country = bfs(i,j) # 연합 리스트
                
                # 인구 이동
                if len(country) > 1:
                    flag = True
                    num = sum([board[y][x] for y,x in country]) // len(country)
                    for y, x in country: # 값 갱신
                        board[y][x] = num
    if not flag:
        break
    cnt += 1
print(cnt)

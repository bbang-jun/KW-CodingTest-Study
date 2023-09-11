from collections import deque
global dq
dq = deque()
N,M = map(int,input().split())

board = []
for _ in range(N):
    board.append(list(map(int,input())))

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(y,x):
    dq.append((y,x))
    while dq:
        y,x = dq.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if board[ny][nx] == 0:
                continue
            if board[ny][nx] == 1: #첫 방문 기록
                dq.append((ny,nx))
                board[ny][nx] = board[y][x] + 1

    return board[N-1][M-1] #반드시 탈출가능한 형태로 준다 함
print(bfs(0,0))

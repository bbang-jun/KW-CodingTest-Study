from collections import deque

# 미로 크기 입력
N, M = map(int, input().split())

# 미로 정보 입력
g = []
for _ in range(N):
    g.append(list(map(int, input())))

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    # Queue 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        
        # 상하좌우 4개 방향 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로를 벗어나지 않는지 검사
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이면 continue
            if g[nx][ny] == 0:
                continue

            if g[nx][ny] == 1:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1
                
    return g[N-1][M-1]


print(bfs(0, 0))

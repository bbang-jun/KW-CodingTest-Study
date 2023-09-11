from collections import deque

# 얼음 틀 크기 입력
N, M = map(int, input().split())

# 얼음 틀 정보 입력
g = []
for i in range(N):
    g.append(list(map(int, input())))

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(graph, x, y):
    # 아이스크림 개수
    cnt = 1
    # Queue 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))

    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 얼음 틀을 벗어나지 않는지 검사
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 얼음이 차 있는 칸만 검사
            if graph[nx][ny] == 1:
                cnt += 1
                # 이미 방문했던 곳은 다시 방문하지 못하게 함
                graph[nx][ny] = 0
                q.append((nx, ny))
    return cnt


result = []

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            # 얼음이 차 있는 칸은 모두 탐색할 때까지 BFS를 수행한 횟수를 구하면 됨
            result.append(bfs(g, i, j))

print(len(result))
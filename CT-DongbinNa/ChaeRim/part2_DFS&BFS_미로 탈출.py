from collections import deque
dq = deque()
n, m = map(int, input().split())

board = [input().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq.append((0,0))
visited[0][0] = 1

while dq:
    x, y = dq.popleft()

    if x == n-1 and y == m-1: # 마지막 좌표라면 !
        print(visited[x][y])
        break

    for i in range(4):
        # 다음 방문 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: # 범위 내에 있다면
            if visited[nx][ny] == 0 and board[nx][ny] == '1': # 방문안했고, 입력받은 맵이 1이라면
                visited[nx][ny] = visited[x][y] +1 # 누적
                dq.append((nx,ny))

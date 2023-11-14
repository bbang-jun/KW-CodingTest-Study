import sys
input = sys.stdin.readline

from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())
# 전체 나라의 정보(N x N)를 입력 받기
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
total_count = 0

def bfs(x, y, index): # BFS => Queue
    united = [(x, y)]
    q = deque([(x, y)])
    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q: # Queue가 빌 때까지
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    if index == n * n:
        break

    total_count += 1

# 인구 이동 횟수 출력
print(total_count)

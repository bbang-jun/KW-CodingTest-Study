from collections import deque


def bfs(maze, N, M, cost):
    queue = deque([(0, 0)])
    cost[0][0] = 1

    while queue:
        i, j = queue.popleft()

        if maze[i][j] == 1:
            if i-1 >= 0 and maze[i-1][j] == 1 and cost[i-1][j] == 0:
                queue.append((i-1, j))
                cost[i-1][j] = cost[i][j] + 1
            if i+1 <= N-1 and maze[i+1][j] == 1 and cost[i+1][j] == 0:
                queue.append((i+1, j))
                cost[i+1][j] = cost[i][j] + 1
            if j-1 >= 0 and maze[i][j-1] == 1 and cost[i][j-1] == 0:
                queue.append((i, j-1))
                cost[i][j-1] = cost[i][j] + 1
            if j+1 <= M-1 and maze[i][j+1] == 1 and cost[i][j+1] == 0:
                queue.append((i, j+1))
                cost[i][j+1] = cost[i][j] + 1

    return cost[N-1][M-1]

N, M = map(int, input().split())
cost = [[0]*M for _ in range(N)]
maze = []

for i in range(N):
    maze.append(list(map(int, input())))

print(bfs(maze, N, M, cost))

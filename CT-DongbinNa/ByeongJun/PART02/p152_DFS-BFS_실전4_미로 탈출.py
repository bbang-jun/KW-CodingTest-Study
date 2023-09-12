from collections import deque


def bfs(maze, N, M, cost):
    queue = deque([(0, 0)]) # 첫 위치를 queue에 넣기
    cost[0][0] = 1 # 칸을 셀 때는 시작 칸도 포함

    while queue:
        i, j = queue.popleft() # queue에서 pop을 하여 인덱스 좌표 얻기

        if maze[i][j] == 1: # 괴물이 없는 부분이고, 이동하지 않은 부분이면 queue에 저장 및 이동 칸 수 갱신
            if i-1 >= 0 and maze[i-1][j] == 1 and cost[i-1][j] == 0: #
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

    return cost[N-1][M-1] # 마지막 칸에 도착하였으므로 해당 위치에서의 이동 칸 수 반환

N, M = map(int, input().split())
cost = [[0]*M for _ in range(N)]
maze = []

for i in range(N):
    maze.append(list(map(int, input())))

print(bfs(maze, N, M, cost))

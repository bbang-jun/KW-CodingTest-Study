import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
# 그래프 초기화
graph = [[0] * n for _ in range(n)]
# 바이러스 정보를 저장하는 리스트
viruses = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = temp[j]
        if temp[j] != 0:
            viruses.append((temp[j], 0, i, j))

# 바이러스는 낮은 번호부터 증식
viruses.sort()
q = deque(viruses)

target_s, target_x, target_y = map(int, input().split())

# BFS
while q:
    temp, second, x, y = q.popleft()
    if second == target_s:
        break
    # 4가지 방향을 모두 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동 여부 체크
        if 0 <= nx < n and 0 <= ny < n:
            # 방문하지 않은(==0) 위치인 경우, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = temp
                q.append((temp, second + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

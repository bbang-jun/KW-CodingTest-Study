N, M = map(int, input().split())
A, B, d = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# N*M 크기의 지도 생성
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

# visited = []
# for i in range(M):
#     for j in range(N):
#         visited[M][N] = False
visited = [[False] * M for _ in range(N)] # 리스트 컴프리헨션

count = 1 # 초기 위치 카운트
visited[A][B] = True # 초기 위해 방문

while True:
    for _ in range(4):
        d = (d - 1) % 4 # 마이너스 인덱스를 이용하여 왼쪽 방향 전환
        nx = A + dx[d] # 방문할 x좌표
        ny = B + dy[d] # 방문할 y좌표

        # 왼쪽 방향에 가보지 않은 육지가 있으면 이동
        if not visited[nx][ny] and maps[nx][ny] == 0:
            visited[nx][ny] = True
            A = nx
            B = ny
            count += 1
            break
    else: # for-else문을 통해 break 시에 실행되지 않도록 함(네 방향 모두 갈 수 없는 경우)
        back_x = A - dx[d]
        back_y = B - dy[d]

        if maps[back_x][back_y] == 1: # 뒤가 바다인 경우 종료
            break
        else: # 뒤로 한 칸 이동
            A = back_x
            B = back_y

print(count)

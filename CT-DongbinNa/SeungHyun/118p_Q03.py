N, M = map(int, input().split())
A, B, d = map(int, input().split())

# 지도 정보 저장
map_list = []
for i in range(N):
    map_list.append(list(map(int, input().split())))
# 방문 여부 저장
visited_list = [[0] * M for _ in range(N)]
# 시작점
visited_list[A][B] = 1

# 서(x좌표 1 감소) -> 남(y좌표 1 증가) -> 동(x좌표 1 증가) -> 북(y좌표 1 감소) -> 서(...)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전 횟수
rotation = 0
result = 1

while True:
    # 왼쪽으로 회전
    d += 1
    # 방향은 0~3까지만 존재
    if d == 4:
        d = 0

    tempX = A + dx[d]
    tempY = B + dy[d]

    if 0 <= tempX < N and 0 <= tempY < M:
        if map_list[tempX][tempY] == 0 and visited_list[tempX][tempY] == 0:
            # 현재 위치 이동 후, 방문 체크
            A, B = tempX, tempY
            visited_list[tempX][tempY] = 1
            rotation = 0

            result += 1
            continue
        else:
            rotation += 1

        # 모든 방향으로 회전한 경우
        if rotation == 4:
            # 방향은 그대로 하고 뒤로 이동
            tempX = A - dx[d]
            tempY = B - dy[d]

            # 뒤로 이동 가능
            if map_list[tempX][tempY] == 0 and visited_list[tempX][tempY] == 0:
                A, B = tempX, tempY
                rotation = 0
            # 뒤로 이동 불가능
            else:
                break

print(result)

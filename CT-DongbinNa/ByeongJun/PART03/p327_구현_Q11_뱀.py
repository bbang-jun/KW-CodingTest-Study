N = int(input())
K = int(input())

apple_location = [[0] * N for _ in range(N)]
board = [[0] * N for _ in range(N)]

# 사과 위치 저장
for i in range(K):
    apple_x, apple_y = map(int, input().split())
    apple_location[apple_x-1][apple_y-1] = 1

L = int(input())
direction_info = []
for i in range(L):
    X, C = input().split()
    X = int(X)
    direction_info.append((X, C))

# 동서남북
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 전환은 효율적인 아이디어를 구상하기 어려워서 답지 참조
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def main():
    direction = time = 0
    x, y = 0, 0
    board[x][y] = 1
    snake_location = [(x, y)]

    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        # board 범위를 나가거나 몸에 부딪히는 경우
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
            if apple_location[nx][ny] == 1:
                board[nx][ny] = 1
                snake_location.append((nx, ny))
            else:
                board[nx][ny] = 1
                snake_location.append((nx, ny))
                del_snake_x, del_snake_y = snake_location.pop(0)
                board[del_snake_x][del_snake_y] = 0
        else:
            break # 부딪히게 되므로 게임 종료
        x, y = nx, ny
        # 이동 후에 전환 수행
        for direction_time, LorR in direction_info:
            if time == direction_time:
                direction = turn(direction, LorR)

    return time

print(main())
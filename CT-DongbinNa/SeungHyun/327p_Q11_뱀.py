from collections import deque
import sys
input = sys.stdin.readline

# 보드의 크기 N
N = int(input())
# 사과의 개수 K
K = int(input())
apple_list = []

# 사과의 위치 정보 입력
for _ in range(K):
    a, b = map(int, input().split())
    apple_list.append((a, b))

# 뱀의 방향 변환 횟수
L = int(input())
# 뱀의 방향 변환 정보 저장
direction_list = []

# 뱀의 방향 변환 정보 입력
for _ in range(L):
    time, dir = input().split()
    direction_list.append((int(time), dir))

# 뱀의 이동(방향 전환)을 위한 리스트
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 뱀의 위치 (1, 1)
snake = deque([(1, 1)])
# 초기 뱀의 방향: 동쪽
snake_dir = 0 
# 경과 시간
result_time = 0

# 무한 루프
while 1:
    result_time += 1

    # 뱀의 머리 위치
    x, y = snake[0]

    # 뱀의 머리를 다음 칸으로 이동
    x += dx[snake_dir]
    y += dy[snake_dir]

    # 종료 조건 1: 벽이랑 부딪히는 경우
    if x < 1 or x > N or y < 1 or y > N in snake:
        break

    # 종료 조건 2: 자기 자신의 몸과 부딪히는 경우
    if (x, y) in snake:
        break

    # 뱀의 머리 위치 업데이트
    snake.appendleft((x, y))

    if (x, y) in apple_list: # 사과를 먹으면 사과 위치 정보만 remove
        apple_list.remove((x, y))
    else: # 사과를 못 먹었으면 꼬리를 자름(=가장 끝 원소를 pop )한다는 것과 같은 의미)
        snake.pop()

    # 방향 전환 시간인지 확인
    for (time, dir) in direction_list:
        if time == result_time:
            if dir == "L": # 왼쪽으로 회전
                snake_dir = (snake_dir - 1) % 4
            else: # 오른쪽으로 회전
                snake_dir = (snake_dir + 1) % 4
        else:
            continue

print(result_time)

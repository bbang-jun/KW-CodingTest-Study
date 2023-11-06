import sys,copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# bfs 상하좌우 탐색
def bfs():
    global new_board
    dq = deque([])
    for y,x in teacher:
        for i in range(4):
            dq.append((y,x,i))
    while dq:
        yy,xx,ii = dq.popleft()
        ny,nx = yy+dy[ii], xx+dx[ii]
        if 0 <= ny < n and 0 <= nx < n:
            if new_board[ny][nx] == 'S':
                return False
            elif new_board[ny][nx] == 'X':
                dq.append((ny,nx,ii))
    return True

# main
if __name__ == "__main__":
    n = int(input())
    graph = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for _ in range(n):
        graph.append(list(map(str,input().split())))

    # 한 줄로 teacher, empty 좌표 저장
    teacher = [(y,x) for y in range(n) for x in range(n) if graph[y][x] == 'T']
    empty = [(y,x) for y in range(n) for x in range(n) if graph[y][x] == 'X']

    # 장애물 O의 위치 3개 뽑아서 새로운 리스트 생성
    for location in combinations(empty,3):
        new_board = copy.deepcopy(graph)

        for y,x in location:
            new_board[y][x] = 'O'

        if bfs():
            print("YES")
            break
    else:
        print("NO")

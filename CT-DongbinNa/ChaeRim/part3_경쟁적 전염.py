import sys, copy
from collections import deque
input = sys.stdin.readline


# N*N 시험관, 바이러스 1~K번
# 번호가 낮은 바이러스 부터 상 하 좌 우 로 1초마다 증식
# S초 후 (x,y)에 존재하는 바이러스 출력 프로그램을 만들자.

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
board = []

def solution(s,row,col):

    new_board = copy.deepcopy(board)
    # virus 위치 저장
    virus = [(i,j,board[i][j]) for i in range(n) for j in range(n) if board[i][j] != 0]
    virus.sort(key=lambda x: x[2]) # 처음에 바이러스 기준 오름차순으로 정렬해줘야함.
    dq = deque(virus)
    time = 0

    while dq:
        if time == s:
            break

        for _ in range(len(dq)): # 이 부분 놓침
            x,y,value = dq.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                # 범위 안에 있을 때
                if 0 <= ny < n and 0 <= nx < n and new_board[nx][ny] == 0:
                    new_board[nx][ny] = value
                    dq.append((nx, ny, value))
        time += 1

    # BFS 완료 후 출력
    print(new_board[row-1][col-1])

if __name__ == "__main__":
    n,k = map(int,input().split())
    for _ in range(n):
        board.append(list(map(int, input().split())))
    s,x,y = map(int,input().split())
    solution(s,x,y)

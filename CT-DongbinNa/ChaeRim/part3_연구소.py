from itertools import combinations
import copy

def solve():
    global answer

    for location in combinations(empty,3): # (0,0) 있는 좌표 3개 뽑음 - 벽의 개수
        new_board = copy.deepcopy(board) # 입력 배열 깊은 복사 (원본 값 안바뀜)

        for y,x in location:
            new_board[y][x] = 1 # 벽 세우기

        # 2인 바이러스 위치 저장 배열
        virus = [(n,m) for n in range(N) for m in range(M) if new_board[n][m]==2]

        # virus가 있는 동안
        while virus:
            y_v,x_v = virus.pop()
            for d in range(4):
                ny, nx = y_v + dy[d], x_v + dx[d]

                # 벽이 없을 때만 new_board 2로 채우기
                if 0 <= ny < N and 0 <= nx < M and new_board[ny][nx] == 0:
                    new_board[ny][nx] = 2
                    virus.append((ny,nx))
        cnt = 0

        # 0 개수 세서 최대값 갱신
        for row in new_board:
            cnt += row.count(0)
        answer = max(answer, cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for _ in range(N):
        board.append(list(map(int,input().split())))

    empty = [(n,m) for n in range(N) for m in range(M) if board[n][m] == 0]
    answer = 0
    solve()
    print(answer)

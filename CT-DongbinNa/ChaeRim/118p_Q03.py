N,M = map(int,input().split())
x,y,d = map(int,input().split())
li = []
# 서 남 동 북 반시계 방향 정의 (왼쪽 쳐다보면 가는방향이 다름)
# 북이면 서로, 서면 남으로, 남이면 동으로, 동이면 북으로
# 따라서 서남동북 순서로 dx, dy설정
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False] * M for _ in range(N)] # 방문 여부 저장 리스트
visited[x][y] = True

for _ in range(N):
    row = list(map(int,input().split()))
    li.append(row)

# 시뮬레이션
cnt = 1 # 처음 방문지점 세놓고 시작
turn = 0
def turn_left():
    global d
    d -= 1
    if d == -1: # 0123 북동남서 북->서로 가려고
        d = 3

while True:
    turn_left() # 1단계 수행
    nx = x + dx[d]
    ny = y + dy[d]

    if nx >= 0 and nx < N and ny >= 0 and ny < M and li[nx][ny] == 0 and visited[nx][ny] == False: # 육지이고 방문하지 않았을 때
        visited[nx][ny] = True
        x, y = nx, ny
        cnt += 1
        turn = 0 #갔으니까 돈거 초기화
        continue #2단계 전진에서 끝 갔으니까 turn검사안함

    else: # 2단계 왼쪽 턴에서 끝
        turn += 1

    if turn == 4: #3단계 유지 뒤로가기
        nx = x - dx[d]
        ny = y - dy[d]
        if li[nx][ny] == 0:
            x,y = nx, ny
            turn = 0 #다시 1단계로 가기위한 회전 초기화
        else:
            break
print(cnt)




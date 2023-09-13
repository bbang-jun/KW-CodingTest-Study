from collections import deque
N,M = map(int,input().split())
ice = []
cnt = 0 #얼음 개수
#visited = [[False]*M for _ in range(N)]

for i in range(N):
    ice.append(list(map(int,input())))

def dfs(y,x):
    if x < 0 or x >= M or y < 0 or y >= N: #범위검사
        return False
    if ice[y][x] == 0:
        ice[y][x] = 1 #방문처리
        dfs(y-1,x) #상
        dfs(y+1,x) #하
        dfs(y,x-1) #좌
        dfs(y,x+1) #우
        return True
    else:
        return False

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            cnt += 1
print(cnt)

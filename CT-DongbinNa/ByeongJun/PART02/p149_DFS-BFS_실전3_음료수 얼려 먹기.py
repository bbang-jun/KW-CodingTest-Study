def dfs(ice, i, j):
    if i < 0 or i >= N or j < 0 or j >= M or ice[i][j] == 1: # 얼음틀 외부 범위 예외처리 및 얼음을 채우지 못하는 경우 에외처리
        return False

    if ice[i][j] == 0:
        ice[i][j] = 1
        dfs(ice, i-1, j) # 상
        dfs(ice, i+1, j) # 하
        dfs(ice, i, j-1) # 좌
        dfs(ice, i, j+1) # 우

    return True


N, M = map(int, input().split())
ice = []
icecream = 0

for i in range(N):
    ice.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if dfs(ice, i, j):
            icecream += 1

print(icecream)
def dfs(ice, i, j):
    if i < 0 or i >= N or j < 0 or j >= M or ice[i][j] == 1: # 얼음틀 외부 범위 예외처리 및 얼음을 채우지 못하는 경우 에외처리
        return False

    if ice[i][j] == 0:
        ice[i][j] = 1 # 방문 처리
        dfs(ice, i-1, j) # 상
        dfs(ice, i+1, j) # 하
        dfs(ice, i, j-1) # 좌
        dfs(ice, i, j+1) # 우

    return True # True 시에 아이스크림 1개 추가


N, M = map(int, input().split())
ice = [] # 그래프 역할의 얼음 틀 리스트 변수
icecream = 0 # 생성되는 아이스크림 개수

for i in range(N):
    ice.append(list(map(int, input()))) # 얼음틀 입력

for i in range(N):
    for j in range(M):
        if dfs(ice, i, j): # dfs 함수를 실행하여 이동할 수 있는 부분을 다 이동하면 아이스크림 개수 증가
            icecream += 1

print(icecream)
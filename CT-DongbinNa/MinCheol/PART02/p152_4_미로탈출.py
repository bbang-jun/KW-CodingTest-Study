from collections import deque

N, M = map(int, input().split())

#declare variables
Arr = []
Q = deque()
Cost = 0
Move = [[-1,0],[0, 1],[1, 0],[0,-1]]

for _ in range(N):
    Arr.append(list(map(int,input())))

def DFS():
    Q.append((0,0))
    while Q:
         X, Y = Q.popleft()
         for i in range(4):
             NewX = X + Move[i][0]
             NewY = Y + Move[i][1]
             if 0<=NewX<M and 0<=NewY<N and Arr[NewY][NewX]==1:
                 Q.append((NewX,NewY))
                 Arr[NewY][NewX]=Arr[Y][X]+1
    return Arr[N-1][M-1]

print(DFS())

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111


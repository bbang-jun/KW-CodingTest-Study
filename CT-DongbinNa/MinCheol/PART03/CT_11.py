# N is size of board
# K is number of apple
# L is number of changing direction
# if snake touch wall or body the game ends
# snake starts on the top and left of the box and length is 1
from collections import deque
Q = deque()
SNAKE = deque()
FINISH = False

MOVE=[(-1,0),(0,1),(1,0),(0,-1)]

N = int(input())

TIME = 1
Direction=1
BOX = [[0]*(N+1) for _ in range(N+1)]

K = int(input())
for _ in range(K):
    A, B = map(int, input().split())
    BOX[A][B]=1
    
L = int(input())
for _ in range(L):
    A, B = map(str,input().split())
    A = int(A)
    Q.append((A,B))


SNAKE.append((1,1))
HEAD = (1,1)
BOX[1][1]=2
for _ in range(L+1):
    if Q:
        A, B = Q.popleft()
        A=A-TIME+1
    else:
        A=999999
    
    for _ in range(A):
        Y, X = MOVE[Direction]
        newY, newX = HEAD
        newX += X
        newY += Y
        if newX<=0 or N<newX or newY<=0 or N<newY or BOX[newY][newX]==2: #have to check snakes body
                FINISH = True
                break
        TIME+=1
        SNAKE.append((newY, newX))
        HEAD=(newY,newX)
        if BOX[newY][newX]!=1:
            oldY, oldX = SNAKE.popleft()
            BOX[oldY][oldX]=0
        BOX[newY][newX]=2
        
    if FINISH==True:
        break
    
    if B=='D':
        Direction+=1
        Direction%=4
    elif B=='L':
        Direction-=1
        Direction%=4

print(TIME)


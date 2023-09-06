A,B = map(int,input().split())

C, D, E = map(int, input().split())

ARR = []
Result = 1
for _ in range (B):
    ARR2 = list(map(int, input().split()))
    ARR.append(ARR2)

Visited = [[False]*A for _ in range (B)]


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

DIR = E
X = C
Y = D
i = 0
Find = True
Visited[Y][X] = True
while True:
    Find = False
    i = DIR
    for i in range (i+4):
        if 0 <= X+dx[i%4] < B and 0 <= Y+dy[i%4] < A and ARR[Y+dy[i%4]][X+dx[i%4]]==0 and Visited[Y+dy[i%4]][X+dx[i%4]]==False:
            DIR = i
            Result+=1
            X = X+dx[i%4]
            Y = Y+dy[i%4]
            Find = True
            Visited[Y][X] = True
            break
    if Find == False:
        break

print(Result)




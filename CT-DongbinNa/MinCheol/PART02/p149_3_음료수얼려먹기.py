from collections import deque

# get N and M
N, M = map(int, input().split())

# decalre Variables
Arr = []
Visited = [[False] * M for _ in range(N)]
Count = 0
Q = deque()
Move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# Get an input about ice box
for _ in range(N):
    Arr.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        # when Meet False
        if not Visited[i][j] and Arr[i][j] == 0:
            Visited[i][j] = True;
            Count += 1;
            Q.append((i, j))

            # visit all adjacent area
            while Q:
                Y, X = Q.popleft()
                for k in range(4):
                    NewX = X + Move[k][0];
                    NewY = Y + Move[k][1]
                    if 0 <= NewX < M and 0 <= NewY < N and not Visited[NewY][NewX] and Arr[NewY][NewX] == 0:
                        Visited[NewY][NewX] = True
                        Q.append((NewY, NewX))

print(Count)

#Summary
#the solution of book didn't use Visited Array rather than put graph 0 into 1

# 4 5
# 00110
# 00011
# 11111
# 00000


# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

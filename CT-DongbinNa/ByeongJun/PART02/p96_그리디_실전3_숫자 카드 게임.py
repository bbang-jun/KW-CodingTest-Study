N, M = map(int, input().split()) # N행, M열

cards = [] # 리스트 선언

answer = 0

for i in range(N): # N개의 줄에 걸쳐 입력받기
    cards.append(list(map(int, input().split()))) # 2차원 리스트
    cards[i].sort()
    if answer < cards[i][0]:
        answer = cards[i][0]

print(answer)
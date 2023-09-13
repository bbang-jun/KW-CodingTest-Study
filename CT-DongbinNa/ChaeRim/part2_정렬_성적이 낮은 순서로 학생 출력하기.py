N=int(input())
li = []
for _ in range(N):
    name, score = map(str,input().split())
    score = int(score)
    li.append((name,score))

li.sort(key=lambda x : x[1]) #점수 기준 정렬

for i in li:
    print(i[0], end=" ")

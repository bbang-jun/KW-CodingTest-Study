N,M,K = map(int,input().split())
num_li = list(map(int,input().split()))
num_li.sort() # O(N)

max_num = num_li[-1]
max_second = num_li[-2]
res, tmp = 0,0

for i in range(M):
    if tmp == K: #횟수도달, tmp 리셋
        tmp = 0
        res += max_second
    else: # tmp세기
        res += max_num
        tmp += 1
print(res)

N,K = map(int,input().split())
cnt = 0
while True:
    if N % K != 0:
        N -= 1 #N <= 100000이라 일일이 빼도 됨
        cnt += 1
    else:
        N /= K
        cnt += 1
    if N == 1:
        break
print(cnt)

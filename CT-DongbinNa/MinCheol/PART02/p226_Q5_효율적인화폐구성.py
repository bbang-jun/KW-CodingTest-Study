from collections import deque
N, M = map(int, input().split())

Q = deque()

Money = [0]*10001
for _ in range(N):
    Temp = int(input())
    Q.append(Temp)

while Q:
    Standard = Q.popleft()
    Temp=0
    Times=0

    #put monetary standard first
    while(Temp<M):
        Temp+=Standard
        Times+=1
        if Money[Temp]!=0:
            Money[Temp] = min(Money[Temp],Times)
        else: 
            Money[Temp]=Times
    
    #check before possible cases
    for i in range(1,M):
        if i%Standard==0:
            continue
        if Money[i]==0:
            continue

        Check = Standard
        Times=0
        while(i+Check<M):
            Times+=1
            if Money[i+Check]==0:
                Money[i+Check] = Money[i]+Times
            else:
                Money[i+Check]=min(Money[i]+Times,Money[i+Check])
            Check+=Standard

if Money[M]==0:
    print(-1)
else:
    print(Money[M])

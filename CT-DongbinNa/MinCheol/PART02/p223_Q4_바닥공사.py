N = int(input())

#in every case there are three ways to move forward in position

Floor=[0]*(N+1)
Floor[1]=1;Floor[2]=3
for i in range(3,N+1):Floor[i]=Floor[i-1]*1 + Floor[i-2]*2
# Floor[3]=(Floor[2]*Floor[1]) + (Floor[1]*2)
# Floor[4]=Floor[3]*Floor[1] + Floor[2]*2
# Floor[5]=Floor[4]*Floor[1] + Floor[3]*2

print(Floor[N])
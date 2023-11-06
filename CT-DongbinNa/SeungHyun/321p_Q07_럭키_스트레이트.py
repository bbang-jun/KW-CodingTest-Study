import sys
input = sys.stdin.readline

N = input()
N1 = N[:len(N)//2]
N2 = N[len(N)//2:]

sumN1 = 0
sumN2 = 0

for i in range(len(N1)):
    sumN1 += int(N1[i])
    
for i in range(len(N2)-1):
    sumN2 += int(N2[i])

if(sumN1 == sumN2):
    print("LUCKY")
else:
    print("READY")
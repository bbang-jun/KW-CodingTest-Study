from collections import deque

#Get an input
INPUT = int(input())
Q1 = deque()
Q2 = deque()

#all case of number is under 30,000
Numbers = [0]*30001
Numbers[INPUT]=1
Q1.append(INPUT)
Times=0

#check every case and append number into Queue
def GetNextNum(num):
    if num%5==0 and Numbers[num//5]==0:Numbers[num//5]=1;Q2.append(num//5)
    if num%3==0 and Numbers[num//3]==0:Numbers[num//3]=1;Q2.append(num//5)
    if num%2==0 and Numbers[num//2]==0:Numbers[num//2]=1;Q2.append(num//2)
    if Numbers[num-1]==0:Numbers[num-1]=1;Q2.append(num-1)

while Numbers[1]==0:
    Times+=1 #increase number of times which executed
    while Q1:Temp = Q1.popleft();GetNextNum(Temp)
    Q1=Q2.copy();Q2.clear()

print(Times)
    

#왕실의 나이트으으으으
In = input()
A = ord(In[0])-96
B = int(In[1])

Count = 0
if A+2 < 9 and B+1 < 9:
    Count+=1
if A+2 < 9 and B-1 > 0:
    Count+=1
if A-2 > 0 and B+1 < 9:
    Count+=1
if A-2 > 0 and B-1 > 0:
    Count+=1
if B+2 < 9 and A+1 < 9:
    Count+=1
if B+2 < 9 and A-1 > 0:
    Count+=1
if B-2 > 0 and A+1 < 9:
    Count+=1
if B-2 > 0 and A-1 > 0:
    Count+=1

print(Count)
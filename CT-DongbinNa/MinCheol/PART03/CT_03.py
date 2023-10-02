#이코테 Q03 문자열뒤집기
Temp = input()
Arr = list(map(int,Temp))

#There is two answer only which can be 1 or 2
Answer1 = Answer2 = 0
#Answer1 is to change array into 0
#Answer2 is to change array into 1
    
if Arr[0]==1:
    Answer1+=1
else:
    Answer2+=1
for i in range(1,len(Arr)):
    if Arr[i-1]==0 and Arr[i]==1:
        Answer1+=1
    elif Arr[i-1]==1 and Arr[i]==0:
        Answer2+=1

print(min(Answer1,Answer2))

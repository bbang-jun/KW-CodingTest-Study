import sys
input = sys.stdin.readline

s=input()
cnt_0,cnt_1 = 0,0

if s[0] == '1':
    cnt_1 += 1
else:
    cnt_0 +=1

for i in range(1,len(s)): #O(len(s)), 10분
    if s[i] == '1' and (s[i] != s[i-1]):
        cnt_1 += 1
    elif s[i] == '0' and (s[i] != s[i-1]):
        cnt_0 += 1

print(min(cnt_0,cnt_1))

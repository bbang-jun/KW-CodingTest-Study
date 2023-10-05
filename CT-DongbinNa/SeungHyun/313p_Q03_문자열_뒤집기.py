import sys
input = sys.stdin.readline

S = input()

changeToZero = 0
changeToOne = 0

if S[0] == '0':
    changeToZero += 1
else:
    changeToOne += 1
    
for i in range(len(S)-2):
    if S[i] != S[i+1]:
        if S[i+1] == '0': 
            changeToZero += 1
        else:
            changeToOne += 1

print(min(changeToZero, changeToOne))
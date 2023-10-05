result = 0 # 결과
zero = 0 # 0에 대한 묶음 갯수
one = 0 # 1에 대한 묶음 갯수

S = list(map(int, input()))
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        continue
    else:
        if S[i] == 0:
            zero+=1
        else:
            one+=1

if S[-1] == 0:
    zero+=1
else:
    one+=1

print(min(zero, one))
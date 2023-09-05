Num = int(input())

Result = 0
for A in range(Num+1):
    for B in range(60):
        for C in range(60):
            if '3' in str(A) or str(B) or str(C):
                Result += 1


print(Result)

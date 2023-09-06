Num = int(input())

Move = input().split()

a=1
b=1

for A in Move:
    if A == 'L':
        if a>1:
            a-=1

    elif A == 'R':
        if a<Num:
            a+=1

    elif A == 'U':
        if b>1:
            b-=1

    elif A == 'D':
        if b<Num:
            b+=1

print(b,a)
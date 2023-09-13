N = int(input())

#답지 참조
Arr = []
for _ in range(N):
    Arr2 = input().split()

    Arr.append((Arr2[0], int(Arr2[1])))

Arr.sort(key=lambda student: student[1])

for Name in Arr:
    print(Name[0],end=' ')
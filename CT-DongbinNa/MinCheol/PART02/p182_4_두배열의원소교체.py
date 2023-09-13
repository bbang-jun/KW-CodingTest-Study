N, K = map(int, input().split())

Arr1 = list(map(int,input().split()))
Arr2 = list(map(int,input().split()))

Arr1.sort()
Arr2.sort(reverse=True)

times = 0

A = 0;B = 0
while True:
    if Arr1[A] < Arr2[B]:
        Arr1[A], Arr2[B] = Arr2[B], Arr1[A]
        A+=1;B+=1;times+=1

    else:
        B+=1

    if times == K or B == N:
        break

Result =0
for i in range(N):
    Result += Arr1[i]

print(Result)
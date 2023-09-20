import sys
input = sys.stdin.readline

N=int(input())
num = set(map(int,input().split()))
M=int(input())
num2 = list(map(int,input().split()))

for i in num2: # O(N)
    # 파이썬 set의 containment 연산 시간복잡도는 O(1)
    if i in num:
        print("yes", end=' ')
    else:
        print("no", end=' ')

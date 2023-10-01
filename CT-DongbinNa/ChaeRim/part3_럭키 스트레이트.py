import sys
input = sys.stdin.readline
n=int(input())

def isLucky(n):
    s = str(n)
    sum1,sum2 = 0,0
    for i in s[:len(s)//2]:
        sum1 += int(i)
    for i in s[len(s)//2:]:
        sum2 += int(i)
    print("LUCKY") if sum1 == sum2 else print("READY")

isLucky(n)

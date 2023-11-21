import sys
import heapq
input = sys.stdin.readline

hq = []
total = 0
n= int(input())
for _ in range(n):
    num = int(input())
    heapq.heappush(hq,num)
while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    c = a+b
    total += c
    heapq.heappush(hq,c)

print(total)

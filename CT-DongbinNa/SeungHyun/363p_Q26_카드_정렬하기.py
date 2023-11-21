import heapq

n = int(input())

min_heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(min_heap, data)

result = 0

while len(min_heap) != 1:
    A = heapq.heappop(min_heap)
    B = heapq.heappop(min_heap)
    sum = A + B
    result += sum
    heapq.heappush(min_heap, sum)
    
print(result)
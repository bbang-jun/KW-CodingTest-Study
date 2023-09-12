N, K = map(int, input().split())

result = 0 # 모든 원소의 합 저장을 위한 변수

# 원소의 개수만큼 정적으로 입력받지 않으므로 list화 하여 입력받기
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 배열 A는 오름차순, 배열 B는 내림차순으로 정렬
array_a.sort() # 1 2 3 4 5
array_b.sort(reverse=True) # 6 6 5 5 5

for i in range(K): # 최대 K번 바꿔치기 연산 수행
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i] # 스와핑 수행

for a in array_a:
    result += a

print(result)
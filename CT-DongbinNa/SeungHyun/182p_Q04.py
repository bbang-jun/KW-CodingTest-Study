N, K = map(int, input().split())

# 입력받는 동시에 원소를 정렬
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse = True)
result = 0

for i in range(K):
    if(A[i] < B[i]):
        # temp 변수 없이 두 원소를 교체
        A[i], B[i] = B[i], A[i]
    else:
        break

# A 배열 원소들의 합
for i in range(N):
    result += A[i]
    
print(result)
N = int(input()) # 동빈이의 부품 개수 N 입력

dongbin_item = list(map(int, input().split())) # 동빈이의 부품 번호 입력

M = int(input()) # 고객 위한 부품 개수 M 입력

customer_item = list(map(int, input().split())) # 고객의 부품 번호 입력

dongbin_item.sort() # 고객이 동빈이의 부품 번호를 확인해야 하므로 동빈이의 부품 번호 정렬

def binary_search(array, target, start, end): # 반복문 이진 탐색 함수
    while start <= end: # 종료 조건
        mid = (start + end) // 2 # 중간 지점
        if array[mid] < target: # 중간값보다 타겟값이 크므로 시작을 중간값 바로 뒤로 설정
            start = mid + 1
        elif array[mid] > target: # 중간값이 타겟값보다 크므로 끝을 중간값 바로 앞으로 설정
            end = mid - 1
        else:
            return "yes " # 중간값과 타겟값이 일치하면 yes
    return "no " # 중간값과 타겟값이 끝까지 일치하지 않으면 no

for i in range(M):
    print(binary_search(dongbin_item, customer_item[i], 0, N - 1), end="")
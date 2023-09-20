# 재귀 함수로 구현한 이진 탐색
def binary_serach(array, target, start, end):
    if start > end:
        return None
    
    # 중간점의 인덱스를 반환해야 함
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # 중간점의 값 > 찾고자 하는 값 -> 왼쪽 확인
    elif array[mid] > target:
        return binary_serach(array, target, start, mid-1)
    # 중간점의 값 < 찾고자 하는 값 -> 오른쪽 확인
    else:
        return binary_serach(array, target, mid+1, end)
    
# 가게에 있는 부품 정보 입력
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 손님이 찾는 부품 정보 입력
M = int(input())
customer = list(map(int, input().split()))

for i in customer:
    # 이진 탐색으로 손님이 찾는 부품이 arr에 존재하는지 확인
    result = binary_serach(arr, i, 0, N-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

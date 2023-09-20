import sys

# 이진 탐색 구현(반복문)
def binary_search(arr, target):
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(arr)

    while(start <= end):
        total = 0
        mid = (start + end) // 2
        
        for i in arr:
            if i > mid:
                total += (i - mid)
        
        # 떡의 양이 충분하면 오른쪽으로 탐색        
        if total >= target:
            start = mid + 1
        # 떡의 양의 모자르면 왼쪽으로 탐색
        else:
            end = mid - 1
    
    # 시작점이 끝점보다 왼쪽으로 가거나 그 반대가 되면 안됨
    return end
    
    
# import sys 활용
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(binary_search(arr, M))
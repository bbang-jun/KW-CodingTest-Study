N, M = map(int, input().split())

each_height = list(map(int, input().split())) # 떡의 개별 높이
each_height.sort() # 떡의 개별 높이 오름차순 정렬
knife_height = 0 # 절단기의 높이

def binary_search(array, target, start, end): # loop로 구현한 이진 탐색
    global knife_height # 절단기의 높이를 전역 변수로 설정
    while start <= end:
        mid = (start + end) // 2
        ricecake_length = 0 # 잘린 떡의 총 길이
        for i in range(N):
            if array[i] - mid <= 0:
                continue
            ricecake_length += array[i] - mid

        if ricecake_length < target: # 잘린 떡의 총 길이가 M보다 작으면 더 많이 잘라야 하므로 더 왼쪽으로 가야함.
            end = mid - 1
        else: # 잘린 떡의 총 길이가 M 이상인 경우 절단기의 높이 최신화
            start = mid + 1
            knife_height = mid
    return knife_height

print(binary_search(each_height, M, 0, each_height[N - 1])) # 답지에서는 each_height[N-1] 대신 max(each_height)
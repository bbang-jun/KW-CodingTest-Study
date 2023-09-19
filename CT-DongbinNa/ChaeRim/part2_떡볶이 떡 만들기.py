import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = list(map(int,input().split()))
start,end = 0, n-1

while start < end: # 반씩 줄여나가 O(logN)
  # 여기서 start <= end조건을 쓰면 안되는지 궁금
  
    tmp = 0
    mid = (start+end)//2

    for i in array:
        if i > mid:
            tmp += i - mid

    if tmp < m:
        end = mid-1
    else: #적어도 M만큼은 얻기위해... 그럼 같거나 크게 잘라야 한다.
        res = mid
        start = mid+1

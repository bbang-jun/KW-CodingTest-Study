#declare function which find target
def binarySearch(start, end, Arr, Target):
    while start <= end:
        mid = (start + end) // 2

        if Arr[mid]==Target:
            return True

        elif Arr[mid]>Target:
            end = mid - 1

        else:
            start = mid + 1

    return None

N = int(input())
Arr_N = list(input().split())
M = int(input())
Arr_M = list(input().split())
Arr_N.sort()

for i in range(M):
    #search item using binarySearch
    Find = binarySearch(0, N-1, Arr_N, Arr_M[i])

    if Find==True:
        print("yes", end=" ")

    else:
        print("no", end=" ")


#this problem is better to use counting sort
#but it has better memory performance
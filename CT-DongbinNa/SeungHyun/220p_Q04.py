import sys

# 입력
N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 결과를 저장하기 위한 배열
dp = [0] * 102

# 초기 설정
# 최소 1칸씩 띄워야 하므로 문제의 조건에 맞게 첫번째와 두번째 항만 직접 계산
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
    # 합이 최대가 되는 경우를 찾아야하므로 마지막으로 입력받은 원소에 이전까지의 결과를 더해야 함
    # 이 문제는 최소 1칸씩 띄워서 계산해야 하므로 마지막에서 두번째로 입력받은 원소는 제외하고 생각하면 됨
    temp = arr[i] + dp[i-2]
    # 따라서 마지막에서 두번째로 입력받은 원소까지의 탐색 결과와 입력받은 원소까지의 탐색결과 중 큰 것을 찾으면 됨
    dp[i] = max(temp, dp[i-1])

# dp[]의 값이 줄어들지는 않기 때문에
# 마지막 탐색에서 max의 인자로 들어가는 2개 중 큰 것을 똑같이 반환하면 됨 
result = dp[N-1]

print(result)
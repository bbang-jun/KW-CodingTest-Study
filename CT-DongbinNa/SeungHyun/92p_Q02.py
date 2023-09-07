# 배열의 크기 N, 숫자가 더해지는 횟수 M, 제한 K
N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()

first = num_list[-1]
second = num_list[-2]

result = 0
tempK = K

while True:
    if M == 0: break

    if tempK != 0:
        result += first
        tempK -= 1
    else:
        result += second
        tempK = K

    M -= 1

print(result)
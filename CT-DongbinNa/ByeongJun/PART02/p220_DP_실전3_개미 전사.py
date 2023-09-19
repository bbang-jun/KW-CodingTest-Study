N = int(input()) # 식량창고의 개수
food = list(map(int, input().split())) # 각 식량창고에 저장된 식량의 개수

dp_table = [0] * 100 # 식량창고의 개수가 최대 100이므로 100개로 설정

for i in range(N):
    if i == 0: # 0번째로 위치한 식량 창고에서 최대로 가능한 식량 개수는 그대로
        dp_table[0] = food[0]
    elif i == 1: # 1번째로 위치한 식량 창고에서 최대한 가능한 식량 개수를 구하기 위해 dp_table[i-2]로 인덱스가 벗어남
        dp_table[1] = max(dp_table[i-1], food[i])
    else:
        dp_table[i] = max(dp_table[i-1], dp_table[i-2]+food[i])

print(dp_table[N-1])
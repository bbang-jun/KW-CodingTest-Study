X = int(input())
dp_table = [0] * 30000

for i in range(2, X+1): # 1로 만드는 것이기 때문에 1은 의미가 없으므로 2부터 시작해서 X까지 반복해야 함
    dp_table[i] = dp_table[i-1]+1 # 이 부분을 통해 최대로 수행되는 수를 저장함.
    if i % 2==0:
        dp_table[i] = min(dp_table[i], dp_table[i//2] +1)
    if i % 3 ==0:
        dp_table[i] = min(dp_table[i], dp_table[i//3] + 1)
    if i % 5 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//5] + 1)
print(dp_table[X])
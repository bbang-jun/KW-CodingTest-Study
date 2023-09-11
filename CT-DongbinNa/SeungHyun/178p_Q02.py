n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

# 내림차순 정렬
num_list = sorted(num_list, reverse=True)

for i in num_list:
    print(i, end = ' ')
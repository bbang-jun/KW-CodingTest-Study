N = int(input())

stu_info = []

for _ in range(N):
    datas = input().split()
    stu_info.append((datas[0], int(datas[1])))

stu_info.sort(key = lambda stu : stu[1])

for stu in stu_info:
    print(stu[0], end =' ')
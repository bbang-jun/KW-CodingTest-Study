N = int(input())

stu_info = []

for _ in range(N):
    datas = input().split()
    stu_info.append((datas[0], int(datas[1]))) # 튜플 형식으로 입력 받은 학생이름, 성적 저장

stu_info.sort(key = lambda stu : stu[1]) # 람다를 이용하여 정렬 수행

for stu in stu_info:
    print(stu[0], end =' ') # 성적이 낮은 순서대로 학생 이름만 출력
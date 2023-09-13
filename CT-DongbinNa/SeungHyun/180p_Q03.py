n = int(input())

student_list = []
for i in range(n):
    # 입력받는 동시에 학생의 이름과 점수를 저장
    student_name, student_score = input().split()
    student_list.append((student_name, int(student_score)))

# sorted()의 key에 람다식을 사용함
student_list = sorted(student_list, key=lambda student: student[1])

for i in student_list:
    print(i[0], end=' ')
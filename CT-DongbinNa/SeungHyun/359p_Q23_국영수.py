import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

# 새로운 정렬 기준
def comparator(student):
    return (-int(student[1]), int(student[2]), -int(student[3]), student[0])

students.sort(key=comparator)

for student in students:
    print(student[0])
    
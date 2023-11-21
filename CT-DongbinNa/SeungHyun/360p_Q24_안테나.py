import sys
input = sys.stdin.readline

n = int(input())
num_list = sorted(list(map(int, input().split())))
median = num_list[(len(num_list)-1)//2]
print(median)

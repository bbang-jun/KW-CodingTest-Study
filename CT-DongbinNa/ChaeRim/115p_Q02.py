loc = input()
row = int(loc[1])
col = int(ord(loc[0])- 97) + 1
cnt = 0

#나이트 이동 방향 (수평,수직)
move_types = [(-2,1), (-2,-1), (2,1), (2,-1), (1,-2), (1,2), (-1,-2), (-1,2)]

for i in move_types:
    nx_row = row + i[0]
    nx_col = col + i[1]

    if nx_row >= 1 and nx_row <= 8 and nx_col >= 1 and nx_col <= 8:
        cnt += 1
print(cnt)

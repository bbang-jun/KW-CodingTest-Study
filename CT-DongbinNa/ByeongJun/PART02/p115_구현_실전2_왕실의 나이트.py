pos = input()

col = ord(pos[0]) - 96 # 열
row = int(pos[1]) # 행

move = [[1, 2], [1, -2], [2, 1], [2, -1],
        [-1, -2], [-1, 2], [-2, -1], [-2, 1]]

pos = [col, row]

count = 0

for i in range(8):
    if col + move[i][0] > 8 or col + move[i][0] < 1 or row + move[i][1] > 8 or row + move[i][1] < 1:
        continue
    count += 1

print(count)
# ord A = 65 a = 97
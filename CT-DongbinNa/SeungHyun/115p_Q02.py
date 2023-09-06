location = input()

col = int(ord(location[0]) - ord('a')) + 1
row = int(location[1])

knight_list = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]

result = 0

for i in knight_list:
    temp_row = row + i[0]
    temp_col = col + i[1]

    if 1 <= temp_row <= 8 and 1 <= temp_col <= 8:
        result += 1

print(result)
left = 0
right = 0

N = list(map(int, input()))

for i in range(len(N)//2):
    left += N[i]
    right += N[-i-1]

if left == right:
    print("LUCKY")
else:
    print("READY")
import sys
input = sys.stdin.readline

# 계산은 연산자 우선순위 무시하고 앞에서 부터
# 나눗셈은 몫만
# 음수 / 양수는 양수로 바꾸고 몫을 취하고 음수로 처리함

n = int(input())
sequence = list(map(int,input().split()))
# + 개수, - 개수 , x 개수, / 개수
add, sub,mul,div = map(int,input().split())
max_value, min_value = -int(1e9), int(1e9)

def dfs(add,sub,mul,div,total,idx):
    global max_value, min_value
    if idx == n:
        max_value = max(max_value,total)
        min_value = min(min_value,total)
        return
    if add:
        dfs(add-1, sub, mul, div, total + sequence[idx], idx + 1)
    if sub:
        dfs(add, sub-1, mul, div, total - sequence[idx], idx + 1)
    if mul:
        dfs(add, sub, mul-1, div, total * sequence[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div-1, int(total / sequence[idx]), idx + 1)

dfs(add, sub, mul, div, sequence[0], 1)
print(max_value)
print(min_value)

counterpart = {'(': ')', ')': '('}

def is_valid(p):
    stack = []
    for char in p:
        if len(stack) == 0:
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    return len(stack) == 0

def split_balanced(p):
    n = 1 if p[0] == '(' else -1
    for i, char in enumerate(p[1:], 1):
        n += 1 if char == '(' else -1
        if n == 0:
            return p[:i + 1], p[i + 1:]

def process(p):
    if p == '':
        return ''

    u, v = split_balanced(p)

    if is_valid(u):
        return u + process(v)
    else:
        s = '(' + process(v) + ')'
        s += ''.join(counterpart[char] for char in u[1:-1])
        return s

def solution(p):
    return process(p)
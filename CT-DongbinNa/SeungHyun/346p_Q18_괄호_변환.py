def balanced_index(p):#균형 잡힌 괄호 문자열의 인덱스를 반환
    count = 0#왼쪽 괄호의 개수
    
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
            
    return -1


def check_proper(p):#올바른 괄호 문자열인지 확인
    count = 0#왼쪽 괄호의 개수
    
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0:# 쌍이 맞지 않는 경우
                return False
            count -= 1
            
    return True# 쌍이 맞는 경우


def solution(p):
    if p == "":
        return ""
        
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if check_proper(u):# 올바른 괄호 문자열일 경우(문제의 3번 조건)
        return u + solution(v)
    else:# 올바른 괄호 문자열이 아닌 경우(문제의 4번 조건)
        answer = "("
        answer += solution(v)
        answer += ")"
        u = u[1:len(u) - 1]# 첫 번째와 마지막 문자를 제거하고
        u = u.replace("(", "temp").replace(")", "(").replace("temp", ")")# 나머지 문자열의 괄호 방향을 뒤집어서
        answer += u#뒤에 붙인다
        return answer

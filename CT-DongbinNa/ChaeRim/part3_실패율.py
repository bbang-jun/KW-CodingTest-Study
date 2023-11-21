from collections import deque
def solution(N, stages):
    answer = []
    dic = dict()
    stages.sort()
    length = len(stages)
    total = [0]*(N+2)
    for i in stages:
        total[i] += 1 # 1단계 실패 사람 1명, 2단계 실패 3명 ...
    for i in range(1,N+1):
        if length == 0:
            dic[i] = 0
            continue
        dic[i] = total[i]/length
        length -= total[i] # 전단계 실패 인원 제거

    result = sorted(dic, key=lambda x: dic[x],reverse=True)
    return result


array = [2,1,2,6,2,4,3,3]
print(solution(5,array))


import sys
from collections import deque
import copy
input = sys.stdin.readline


# N개의 강의를 수강하는 최소시간, 선수과목 -> 위상 정렬
n = int(input())
indegree = [0] * (n+1) # 진입 차수
graph = [[] for i in range(n+1)] #간선 정보 연결 리스트
times = [0]*(n+1) #강의 시간 담는 리스트

for i in range(1,n+1): #O(n)
    tmp = list(map(int,input().split()))
    times[i] = tmp[0] # 맨 첫번째 요소

    for j in tmp[1:-1]: # -1전까지 슬라이싱 후 차수 증가
        indegree[i] += 1
        graph[j].append(i)


def topology_sort():
    result = copy.deepcopy(times)
    dq = deque()

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1,n+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        # result.append(now)

        for i in graph[now]:
            # 노드에서 결과가 더 오래걸리는 것을 채택
            result[i] = max(result[i], result[now]+times[i])
            indegree[i] -=1

            if indegree[i] == 0:
                dq.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()

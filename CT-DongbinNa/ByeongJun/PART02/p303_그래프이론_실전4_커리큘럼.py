# 선후수 관계가 있으므로 위상 정렬을 사용해야 함
# 동시에 강의 수강이 가능하므로, 예시에서 1번 강의와 2번 강의를 동시에 수강하고, 3번 강의 수강 시에 최소 70시간
from collections import deque
N = int(input()) # N: 강의의 수
import copy

indegree = [0] * (N + 1)
time = [0] * (N + 1)
# time_result = [0] * (N + 1) # 결과
graph = [[] for i in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split())) # 4 1 -1
    time[i] = temp[0]
    #for j in range(1, len(temp) + 1):
    for j in temp[1:-1]:
        #if temp[j] == -1:
         #   break
        indegree[i] += 1
        graph[j].append(i)

# indegree가 0이면 해당 시간 그대로 출력
# indegree가 0 이상이면 선수 과목들 중 최대 시간 + 후수 과목 시간
def topology_sort():
    time_result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # result.append(now)
        for i in graph[now]:
            time_result[i] = max(time_result[i], time_result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in time_result[1:len(time_result)+1]:
        print(i)

topology_sort()


import heapq
def solution(food_times, k):
    hq = []
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 탐색해야함
    for i in range(len(food_times)):
        # 음식시간, 음식번호로 힙에 삽입
        heapq.heappush(hq,(food_times[i], i+1))

    # 먹는데 사용한시간, 직전에 먹은 시간
    use, previous = 0,0
    length = len(food_times)

    # 먹기위해쓴 시간 + (현재음식시간 - 이전 음식시간) 전체가 k보다 크면
    while (use + ((hq[0][0] - previous) *length) <= k):

        # 현재 음식 제거
        now = heapq.heappop(hq)[0]
        # 전체 시간에 현재 음식 모두 먹는 시간
        use += (now - previous)  * length
        length -=1
        previous = now

    #음식번호 기준 정렬
    answer = sorted(hq, key=lambda x:x[1])

    return answer[(k-use)%length][1]

# food_times = [3,1,2]
# k = 5
# print(solution(food_times,k))

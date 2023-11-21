def solution(N, stages):
    failure_rate_list = []

    for stage in range(1, N + 1):
        total_users = len(stages)
        current_stage_users = stages.count(stage)

        # 각 스테이지 별 실패율 구하기
        if total_users == 0:
            failure_rate = 0
        else:
            failure_rate = current_stage_users / total_users
        
        failure_rate_list.append((stage, failure_rate))

        # 계산한 스테이지 별 실패율을 리스트에 추가하기
        next_stages = []

        for s in stages:
            if s != stage:
                next_stages.append(s)

        stages = next_stages
        
    # 정렬 후 출력
    answer = [stage for stage, _ in sorted(failure_rate_list, key=lambda x: x[1], reverse=True)]
    return answer

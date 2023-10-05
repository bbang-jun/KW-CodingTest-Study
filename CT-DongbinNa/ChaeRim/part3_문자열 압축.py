def solution(s):
    answer = 1001

    # 1개단위부터 전체 길이 절반개수까지 자를것이다. 
    # 예를 들어 문자열 길이가 6이면 3개까지 자를 수 있다. 

    for i in range(1, len(s) // 2 + 2):  # len(s) == 1일때도 고려
        tmp = s[:i]
        tmp_s = ''
        cnt = 1

        # 정해진 길이만큼 자르려면.. i개부터 i만큼, (i+n)개의 
        # 문자열을 슬라이싱 해야한다. 예를 들어 길이가 2,8, 까지 2만큼 4번
        # 길이가 3이면 15+3 18까지 3,6,9,12,15, 5번 .. 
        for j in range(i, len(s) + i, i):
            if tmp == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    tmp_s += str(cnt) + tmp
                else:  # 자른 값 그대로 넣는다
                    tmp_s += tmp
                tmp = s[j:j + i]
                cnt = 1
        answer = min(answer, len(tmp_s))

    return answer

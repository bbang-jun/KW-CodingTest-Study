def solution(s):
    answer = 0
    result = []

    for i in range(1, len(s) + 1):
        count = 1
        pattern = s[0:i]
        temp = ""
        for j in range(i, len(s), i):
            if pattern == s[j:j + i]:
                count += 1
            else:
                if count > 1:
                    temp += str(count)
                temp += pattern
                pattern = s[j:j + i]
                count = 1
        if count > 1:
            temp += str(count)
        temp += pattern
        result.append(len(temp))

    answer = min(result)
    return answer

# range(0, len(s), i)로 했으나 test case 5번째에서 x도 1개가 증가되어 결과값이 18이 됨. -> 처음 것도 무조건 카운트 됨
# 따라서 range(i, len(s), i)로 설정해서 풀이
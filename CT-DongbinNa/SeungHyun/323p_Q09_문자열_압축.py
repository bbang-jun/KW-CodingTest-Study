def solution(s):
    answer = len(s)

    for i in range(1, (len(s)//2)+1):
        compressed = ""
        token = s[0:i]
        count = 1

        for j in range(i, len(s), i):
            if token == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    compressed += (str(count) + token)
                else:
                    compressed += token
                token = s[j:j+i]
                count = 1

        if count >= 2:
            compressed += (str(count) + token)
        else:
            compressed += token

        answer = min(answer, len(compressed))

    return answer
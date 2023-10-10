def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return 0
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return 0
    return 1

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        if operate == 0:
            answer.remove([x, y, stuff])
            if possible(answer) == 0:
                answer.append([x, y, stuff])

        if operate == 1:
            answer.append([x, y, stuff])
            if possible(answer) == 0:
                answer.remove([x, y, stuff])

    sorted(answer)

    return answer
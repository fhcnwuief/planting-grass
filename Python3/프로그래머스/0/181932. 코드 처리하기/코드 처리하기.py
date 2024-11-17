def solution(code):
    answer = ''
    mode = 0
    for idx, char in enumerate(code):
        if mode == 0 and char != '1' and idx % 2 == 0:
            answer += char
        elif mode == 1 and char != '1' and idx % 2 != 0:
            answer += char
        elif char == '1':
            mode = 1 - mode
    if len(answer) == 0:
        return "EMPTY"

    return answer
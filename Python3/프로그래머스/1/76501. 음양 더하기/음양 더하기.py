def solution(absolutes, signs):
    answer = 0
    for idx, num in enumerate (absolutes):
        if signs[idx] == False:
            num *= -1
        answer += num
    return answer
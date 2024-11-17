def solution(sides):
    answer = 0
    if max(sides)<(sum(sides)-max(sides)):
        answer = 1
    else:
        answer = 2
    return answer
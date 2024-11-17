def solution(dots):
    answer = 1
    a = max(dots)[0] - min(dots)[0]
    b = max(dots)[1] - min(dots)[1]
    return a * b
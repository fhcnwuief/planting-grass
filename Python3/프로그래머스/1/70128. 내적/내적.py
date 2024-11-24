def solution(a, b):
    answer = 0
    for idx, num in enumerate(a):
        answer += a[idx] * b[idx]
#   return sum([x*y for x, y in zip(a,b)])
    return answer
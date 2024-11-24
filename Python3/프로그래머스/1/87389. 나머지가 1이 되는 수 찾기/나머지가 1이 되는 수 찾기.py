def solution(n):
    return min([x for x in range(1, n+1) if n % x == 1])
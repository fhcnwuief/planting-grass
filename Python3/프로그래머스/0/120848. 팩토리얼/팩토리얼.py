def solution(n):
    answer = 10
    num = 1
    for i in range(2,11):
        num *= i
        if num > n:
            return i-1
            
    return answer
def solution(n):
    answer = 0
    i=10
    sum=0
    while n:
        sum = sum + n%i
        n = n //i
    
    return sum
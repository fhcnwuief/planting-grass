def solution(n):
    answer = 0
    i=1
    while(i<n/2):
        if n/i==i:
            answer = 1
            break
        else:
            answer = 2
        i = i + 1
    return answer
def solution(num,total):
    d = 0
    for i in range(1,num-1):
        d += i
    div = (total-d) // num
    answer = [n for n in range(div,div+num)]
    return answer
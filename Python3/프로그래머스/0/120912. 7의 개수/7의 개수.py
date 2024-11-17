def solution(array):
    answer = 0
    a = 7
    for i in array :
        if str(a) in str(i):
            answer += str(i).count(str(a))
    return answer
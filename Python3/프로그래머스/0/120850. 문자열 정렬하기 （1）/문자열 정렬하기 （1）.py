def solution(my_string):
    answer = []
    num = ["0","1","2","3","4","5","6","7","8","9"]
    for x in my_string:
        if x in num:
            answer.append(int(num[int(x)]))
    answer.sort()
    return answer
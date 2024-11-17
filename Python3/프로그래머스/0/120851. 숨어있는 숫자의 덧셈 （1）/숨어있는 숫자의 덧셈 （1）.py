def solution(my_string):
    answer = 0
    for i in range(0,len(my_string)):
        if 48 <=ord(my_string[i]) and ord(my_string[i])<=57:
            answer = answer + int(my_string[i])
    return answer
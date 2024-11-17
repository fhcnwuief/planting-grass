def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if letter == i :
            my_string = my_string.replace(i,'')
    return my_string
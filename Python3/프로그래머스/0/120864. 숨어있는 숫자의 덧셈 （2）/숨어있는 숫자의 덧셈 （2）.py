def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    #map(int,리스트) = 리스트의 모든 요소를 int로 변경
    return sum(list(map(int,my_string)))
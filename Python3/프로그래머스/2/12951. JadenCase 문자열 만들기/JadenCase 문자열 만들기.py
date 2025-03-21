def solution(s):
    s_lst = s.split(" ")
    for i in s_lst:
         s_lst[s_lst.index(i)] = i.capitalize()
    return ' '.join(s_lst)
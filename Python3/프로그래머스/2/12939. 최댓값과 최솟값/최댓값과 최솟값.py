def solution(s):
    lst = list(map(int,s.split(" ")))
    return ' '.join([str(min(lst)),str(max(lst))])
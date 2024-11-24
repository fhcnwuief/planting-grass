def solution(s):
    p_c,y_c = 0,0
    # 모두 소문자로 바꿔버리는거!!
    p_c = s.lower().count('p')
    y_c = s.lower().count('y')
    return True if p_c == y_c else False
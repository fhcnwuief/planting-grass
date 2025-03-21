def solution(s):
    zero_c, one_c, total_c = 0,0,0
    while (s != '1'):
        zero_c += s.count('0')
        one_c = s.count('1')
        s = str(format(one_c,'b'))
        total_c += 1
    return total_c, zero_c
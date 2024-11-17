def solution(polynomial):
    answer = ''
    polynomial = polynomial.replace(' ','').split('+')
    # a ->계수 b -> 상수
    a, b = 0, 0
    for i in polynomial:
        if 'x' in i:
            # x가 있고 길이가 1보다 길다 = 계수가 붙어있음
            if len(i) > 1:
                a += int(i[:-1])
            else:
                a +=1
        else:
            b += int(i)
    
    if a == 0:
        return '{}'.format(b)
    elif a == 1:
        if b == 0:
            return 'x'
        elif b != 0:
            return 'x + {}'.format(b)
    elif a > 1:
        if b == 0:
            return '{}x'.format(a)
        elif b != 0:
            return '{}x + {}'.format(a, b)
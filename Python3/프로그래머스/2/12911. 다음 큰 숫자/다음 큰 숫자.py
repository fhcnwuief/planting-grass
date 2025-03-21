def solution(n):
    one_c = format(n,'b').count('1')
    while (1):
        n += 1
        if format(n,'b').count('1') == one_c:
            break
    return n
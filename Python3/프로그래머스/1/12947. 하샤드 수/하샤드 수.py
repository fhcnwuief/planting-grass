def solution(x):
    s_num = 0
    for num in str(x):
        s_num += int(num)
    return True if x%s_num == 0 else False
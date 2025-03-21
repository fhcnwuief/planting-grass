def solution(s):
    # # ( = 1, ) = -1
    # count = 0
    # for c in s:
    #     if c == '(':
    #         count += 1
    #     elif c == ')':
    #         count -= 1
    # return True if count == 0 else False
    a_list = []
    for c in s:
        if c == '(':
            a_list.append(c)
        else:
            if a_list == []:
                return False
            else:
                a_list.pop()
    
    if a_list != []:
        return False
    
    return True
            
    
    
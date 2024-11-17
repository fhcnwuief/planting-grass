def solution(common):
    if common[1]-common[0] == common[2]-common[1]:
        min = (common[1]-common[0])
        return common[-1] + min
    else:
        mul = common[1] // common[0]
        return common[-1] * mul
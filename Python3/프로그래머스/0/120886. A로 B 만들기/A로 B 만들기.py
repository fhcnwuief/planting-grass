def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    
    for i in range(0,len(before)):
        if before[i] != after[i]:
            return 0
    return 1
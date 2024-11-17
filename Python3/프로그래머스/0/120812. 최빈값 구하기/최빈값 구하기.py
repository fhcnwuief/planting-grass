def solution(array):
    answer = 0
    cnt = [0]*(max(array)+1)
    
    for i in array:
        cnt[i] = cnt[i] + 1
    
    maxcount = max(cnt)
    
    x=0
    for i in cnt:
        if i==maxcount:
            x=x+1
            
    if x!=1:
        answer = -1
    else:
        answer = cnt.index(max(cnt))
    
    return answer
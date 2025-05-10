def solution(topping):
    
    answer = 0  
    
    left = {}
    right = {}
    
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
    
    for idx in range(len(topping)-1):
        
        if topping[idx] in left:
            left[topping[idx]] += 1            
        else:
            left[topping[idx]] = 1
            
        right[topping[idx]] -= 1
        
        if right[topping[idx]] == 0:
            del right[topping[idx]]
            
        
        if len(right) == len(left):
            answer += 1
        
    return answer
    
    
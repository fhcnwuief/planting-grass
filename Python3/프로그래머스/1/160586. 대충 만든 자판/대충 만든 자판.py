def solution(keymap, targets):
    answer = []

    for word in targets:    
        cnt = 0          
        
        for char in word:   
            flag = False    
            time = 101      
            
            for key in keymap:      
                if char in key:	
                    time = min(key.index(char)+1, time)
                    flag = True    
                    
            if not flag:           
                cnt = -1;break  
            
            cnt += time          
            
        answer.append(cnt)        
    
    return answer
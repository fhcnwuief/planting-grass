def solution(n,a,b):
    answer = 1
    
    for cnt in range(n):
        
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        if a == b :
            return answer
        
        answer += 1
    
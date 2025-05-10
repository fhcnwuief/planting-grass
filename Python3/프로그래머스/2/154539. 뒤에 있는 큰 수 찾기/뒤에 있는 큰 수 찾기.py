def solution(numbers):
    # answer = []
    # only for testcase
    # for idx in range(len(numbers)):
    #     n_list = numbers[idx+1:len(numbers)]
    #     if len(n_list) == 0:
    #         answer.append(-1)            
    #     for num in n_list:
    #         if numbers[idx] >= max(n_list):
    #             answer.append(-1)
    #             break
    #         if numbers[idx] < num:
    #             answer.append(num)
    #             break
                
    answer = [-1]*len(numbers)
    
    stack = []
    
    for index in range(len(numbers)):
    
        target = numbers[index]
        
        while stack and numbers[stack[-1]]<target:
            answer[stack.pop()]=target
            
        stack.append(index)
                
    return answer
# https://yinq.tistory.com/187
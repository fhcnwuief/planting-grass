def solution(elements):
    answer = set()
    n_element = elements + elements
    # 1 2 3 4 5
    for l in range(1,len(elements)+1):
        for i in range(len(elements)): 
            # 길이별 연속수열..
            # print(n_element[i:i+l])
            
            # 중복 제거 삽입
            #if sum(n_element[i:i+l]) not in answer:
            # answer.append(sum(n_element[i:i+l]))
            answer.add(sum(n_element[i:i+l]))
                
        
    return len(answer)
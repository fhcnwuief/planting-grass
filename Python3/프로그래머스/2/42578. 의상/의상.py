def solution(clothes):
    
    clothes_dict = {}
    answer = 1
    
    for item in clothes:
        i_name = item[0]
        i_type = item[1]
        
        if i_type in clothes_dict:
            clothes_dict[i_type] += 1
        else:
            clothes_dict[i_type] = 1
            
    for key, value in clothes_dict.items():
        answer *= value+1
    
    return answer - 1
def solution(want, number, discount):
    answer = 0
    c_want = [0 for i in range (len(want))]
    cnt = 0
    # sum(number) = 10
    for i in range(len(discount)):
        for idx in range(len(want)):
            c_want[idx] = discount[i:i+sum(number)].count(want[idx])
        if c_want == number:
            cnt += 1
    return cnt if cnt != 0 else 0

            
    
    

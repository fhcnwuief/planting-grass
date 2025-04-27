def solution(n, words):
    # [번호, 차례]
    answer = []
    
    for idx in range(1, len(words)):
        if(words[idx-1][-1] != words[idx][0]) or (words[idx] in words[:idx]):
            return [(idx%n) + 1,(idx//n)+1]
    return [0,0]
            


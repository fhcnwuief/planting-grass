from itertools import permutations

def solution(babbling):
    answer = 0
    a,b,c,d = "aya","ye","woo","ma"
    arr = [a,b,c,d]
    bab = []
    for i in range(1,len(arr)+1):
        for word in permutations(arr,i):
            bab.append(''.join(word))

    for word in babbling:
        if word in bab:
                answer += 1
    return answer
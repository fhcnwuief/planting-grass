def solution(k, tangerine):
    answer = 0
    cnt = [0 for _ in range(max(tangerine))]
    for i in tangerine:
        cnt[i-1] += 1
    cnt.sort(reverse=True)
    for i in cnt:
        k -= i
        answer += 1 
        if (k <= 0):
            return answer
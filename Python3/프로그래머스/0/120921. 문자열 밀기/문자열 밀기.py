def solution(A, B):
    answer = 0
    cnt = 0
    while A != B:
        A = A[-1]+A[:-1]
        answer += 1
        cnt += 1
        if cnt == len(A):
            return -1
    return answer
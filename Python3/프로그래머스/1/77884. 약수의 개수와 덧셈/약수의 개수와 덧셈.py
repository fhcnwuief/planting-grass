def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:  # 약수의 개수 판별
                cnt += 1
        if cnt % 2 == 0:    # 짝수
            answer += i
        else:               # 홀수
            answer -= i
                
    return answer
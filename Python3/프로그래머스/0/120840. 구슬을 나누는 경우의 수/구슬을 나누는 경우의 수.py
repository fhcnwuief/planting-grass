def solution(balls, share):
    answer = 0
    a = 1
    b = 1
    #분자 - balls 부터 share 까지의 곱
    #분모 - balls-share 부터 1까지의 곱
    for i in range(share+1,balls+1):
        a *=i
    for j in range(balls-share,0,-1):
        b *=j
    return a/b
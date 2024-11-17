def solution(num_list):
    answer = []
    cnt1 = 0
    cnt2 = 0
    for i in num_list:
        if i%2==0:
            cnt2 = cnt2 + 1
        else:
            cnt1 = cnt1 + 1
    return [cnt2, cnt1]
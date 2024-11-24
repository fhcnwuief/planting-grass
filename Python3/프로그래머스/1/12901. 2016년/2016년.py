def solution(a, b):
    answer = 4
    # 1월 0일은 목요일 -> 4
    # 일 0 월 1 화 2 수 3 목 4 금 5 토 6
    # 배열?
    # 1월 0 2월 1 
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(a-1):
        answer += month[i]
    answer += b
    
    return day[answer%7]
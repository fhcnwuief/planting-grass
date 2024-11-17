def solution(hp):
    answer = 0
    ant=[5,3,1]
    for i in ant:
        answer += hp//i
        hp %=i
    return answer
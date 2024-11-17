import statistics

def solution(score):
    answer = []
    avg = [statistics.mean(score[i]) for i in range(len(score))]
    list = sorted(avg,reverse=True)
    for i in avg:
        answer.append(list.index(i)+1)
    return answer

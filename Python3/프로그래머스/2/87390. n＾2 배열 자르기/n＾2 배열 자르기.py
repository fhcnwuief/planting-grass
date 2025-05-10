def solution(n, left, right):
    # answer = []
    # for i in range(n):
    #     for j in range(n):
    #         answer.append(max(i+1,j+1))
    # return answer[left:right+1]
    
    answer = []

    for k in range(left, right + 1):
        
        row = k // n
        col = k % n

        value = max(row, col) + 1

        answer.append(value)

    return answer

'''
어떻게 계산하냐면요, 1차원 배열의 어떤 0-based 인덱스 k에 해당하는 값이 무엇인지 바로 알아낼 수 있어요.
인덱스 k는 k // n 번째 행 (0-based)의 k % n 번째 열 (0-based)에 해당하는 칸입니다.
이 칸의 1-based 행 번호는 (k // n) + 1이고, 1-based 열 번호는 (k % n) + 1이죠.
앞에서 이야기했듯이, 1-based 인덱스 (r, c) 칸의 값은 max(r, c)와 같으므로, 0-based 인덱스 k의 값은 max((k // n) + 1, (k % n) + 1)이 됩니다.

'''
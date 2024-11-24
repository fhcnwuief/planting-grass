def solution(s):
    answer = []
    # 쌍으로 하는게 편하지 않을까..?
    dic = {}
    for idx, txt in enumerate(list(s)):
        if txt not in dic:
            answer.append(-1)
            # 단어의 인덱스? 정보? 저장 (b:0,a:1,...처럼 저장되서 키값이 영어, 밸류값을 이용한 계산 만들기)
            dic[txt] = idx
        else:
            answer.append(idx - dic[txt])
            dic[txt] = idx
    return answer
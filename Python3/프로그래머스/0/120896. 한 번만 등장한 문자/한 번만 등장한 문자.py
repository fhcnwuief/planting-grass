def solution(s):
    freq_dict = {}
    
    for word in list(s):
        if word not in freq_dict.keys():
            freq_dict[word] = 0
        freq_dict[word] += 1
    # items() - 키와 값을 쌍으로 리턴
    # word[0] = 키, word[1] = 값
    one_words = sorted([word[0] for word in freq_dict.items() if word[1] == 1])
    
    return "".join(one_words)
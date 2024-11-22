import re

def solution(new_id):
    # 정규 표현식 문제
    
    #1
    new_id = new_id.lower()
    #2
    new_id = re.sub(r'[^a-z0-9\-_\.]', '', new_id)
    #3
    new_id = re.sub(r'\.{2,}', '.', new_id)
    #4
    new_id = re.sub(r'^\.|\.$', '', new_id)
    #5
    if new_id == '': new_id = 'a'
    #6
    new_id = new_id[:15]
    new_id = re.sub(r'^|\.$', '', new_id)
    #7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
def solution(keyinput, board):
    # 제한 크기 지정
    xlim = (board[0]-1)//2
    ylim = (board[1]-1)//2
    answer = []
    word = {"up":[0,1],"down":[0,-1],"left" : [-1,0],"right":[1,0]}   
    # 초기값
    x=y=0
    for dc in keyinput:
        # 배열 값 순서대로 x,y 넣기
        o,t = word[dc]
        # 이동
        a,b = x+o,y+t
        
        if abs(a)<=xlim and abs(b)<=ylim:
            x,y = a,b
    
    return [x,y]
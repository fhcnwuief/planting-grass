def solution(numbers):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", 
           "six", "seven", "eight", "nine" ]
    for idx,i in enumerate (num):
        #replace(old,new,[count])
        #old - 현재 변경하고 싶은 문자
        #new - 새로 바꿀 문자
        #[count] - 변경할 횟수. 기본값은 -1(전체를 의미)
        numbers = numbers.replace(i,str(idx))
    return int(numbers)
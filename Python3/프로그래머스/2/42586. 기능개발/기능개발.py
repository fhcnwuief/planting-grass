import math

def solution(progresses, speeds):
    answer = []
    work_flow = [0 for _ in range(len(progresses))]
    for num in range(len(progresses)):
        # 작업하는데 걸리는 시간
        work_flow[num] = math.ceil((100 - progresses[num])/speeds[num])
    print("work_flow = " , work_flow)
    
    st = []
    for idx in range(len(work_flow)):
        if len(st) == 0:
            st.append(work_flow[idx])
            
        else:
            compare = max(st)
            
            if compare < work_flow[idx]:
                answer.append(len(st))
            
                for l in range(len(st)):
                    st.pop()
            
                st.append(work_flow[idx])
                
            elif compare >= work_flow[idx]:
                st.append(work_flow[idx])
                
        if idx == len(work_flow)-1:
            answer.append(len(st))

    return answer
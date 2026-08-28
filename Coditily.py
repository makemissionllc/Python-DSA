def solution(A):
    lt = 0
    rt = len(A) - 1
    dc = 0
    
    while lt <= rt:
        dc += 1
        
        vl = abs(A[lt])
        vr = abs(A[rt])
        
        if vl > vr:
            while lt <= rt and abs(A[lt]) == vl:
                lt += 1
        elif vr > vl:
            while lt <= rt and abs(A[rt]) == vr:
                rt -= 1
        else:
            while lt <= rt and abs(A[lt]) == vl:
                lt += 1
            while lt <= rt and abs(A[rt]) == vr:
                rt -= 1
                
    return dc
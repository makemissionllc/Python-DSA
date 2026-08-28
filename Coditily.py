def solution(A):
    left = 0
    right = len(A) - 1
    dc = 0
    
    while left <= right:
        dc += 1
        
        vl = abs(A[left])
        vr = abs(A[right])
        
        if vl > vr:
            while left <= right and abs(A[left]) == vl:
                left += 1
        elif vr > vl:
            while left <= right and abs(A[right]) == vr:
                right -= 1
        else:
            while left <= right and abs(A[left]) == vl:
                left += 1
            while left <= right and abs(A[right]) == vr:
                right -= 1
                
    return dc
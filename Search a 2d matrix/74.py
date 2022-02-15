from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    targetList = []
    L = 0
    R = len(matrix) - 1

    while L <= R:
        m = (L+R)//2
        if matrix[m][0] <= target and matrix[m][-1] >= target:
            targetList = matrix[m]
            break
        elif matrix[m][-1] < target:
            L = m+1
        elif matrix[m][0] > target:
            R = m-1

    L = 0
    R = len(targetList) - 1

    while L <= R:
        m = (L+R)//2
        if targetList[m] < target:
            L = m+1
        elif targetList[m] > target:
            R = m-1
        else:
            return True


    
    return False
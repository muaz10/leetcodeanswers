from typing import List

def sumOfUnique(nums: List[int]) -> int:
    visited = set()
    unique = set()
    for i in nums:
        if i in visited:
            unique.discard(i)
        else:
            visited.add(i)
            unique.add(i)
    
    sum = 0
    for i in unique:
        sum += i

    return sum

nums = [1,2,3,4,5]
print(sumOfUnique(nums))
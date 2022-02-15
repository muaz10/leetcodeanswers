from typing import List

def maxProduct(nums: List[int]) -> int:
    maxval = 0
    scndmax = 0

    for i in range(len(nums)):
        if nums[i] > nums[maxval]:
            maxval = i
            
    if maxval == 0:
        scndmax = 1

    for i in range(len(nums)):
        if nums[i] > nums[scndmax] and i != maxval:
            scndmax = i
    print(maxval)
    print(scndmax)
    
    return (nums[maxval]-1)*(nums[scndmax]-1)

def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        val = nums.pop(-1)
        val2 = nums.pop(-1)
        
        return (val-1)*(val2-1)
    
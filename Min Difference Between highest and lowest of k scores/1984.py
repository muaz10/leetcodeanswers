def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    if k == 1:
        return 0
    mini = float('inf')
    for i in range(len(nums)):
        if i+k-1 < len(nums):
            if nums[i+k-1]-nums[i] < mini:
                mini = nums[i+k-1]-nums[i]
                
    return mini

def minimumDifference2(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    ans=float("inf")
    
    for i in range(len(nums)-k+1):
        ans = min(ans,(nums[i]-nums[i+k-1]))
    return ans
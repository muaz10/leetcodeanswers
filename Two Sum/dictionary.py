class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
            
        for i in range(len(nums)):
            if target - nums[i] in dictionary and dictionary[target - nums[i]] != i:
                solution = [dictionary[target - nums[i]], i]
        
        return solution
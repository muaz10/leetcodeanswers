from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
  dic = {}
  for i in range(len(nums)):
    if nums[i] in dic:
      return True
    else:
      dic[nums[i]] = True
  
  return False
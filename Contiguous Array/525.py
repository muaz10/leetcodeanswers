from typing import List
def contiguous_array(nums: List[int]):
  dic = {}
  count = 0
  l=len(nums)
  for i in range(l):
    dic[i] = nums[i]
    if(nums[i]==0):
      count+=1
    
  if(l-count==count):
    return l

  for i in range(0,l,1):
    

  return -1

nums = [0,1,0,1,0]
print(contiguous_array(nums))
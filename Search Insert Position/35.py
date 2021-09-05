from typing import List
def search_insert_pos(nums: List[int], target: int):
  low=0
  high=len(nums)-1

  while high>=low:
    mid=(high+low)//2
    if nums[mid]==target:
      return mid
    elif nums[mid]>target:
      high=mid-1
    else:
      low=mid+1
  return low
    

nums = [1,3,5,6,7,9,11,12]
target = 2
print(search_insert_pos(nums, target))
# print(7//2+1)
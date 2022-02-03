from typing import List

def search(nums: List[int], target: int) -> int:
  def bs(left: int, right: int, search: int, pivot: int):
    if nums[pivot] == search:
      return pivot
    if left == right:
      return -1
    if search < nums[pivot]:
      nextPivot = (left + pivot-1)//2 + (left + pivot-1)%2
      return bs(left, pivot-1, search, nextPivot)
    elif search > nums[pivot]:
      nextPivot = (pivot + right)//2 + (pivot + right)%2
      return bs(pivot, right, search, nextPivot)

  return bs(0, len(nums)-1, target, len(nums)//2)

nums = [-1,0,3,5,9,12]
target = 5

print(search(nums, target))

from typing import List

def maxSubArray(nums: List[int]) -> int:
  max = 0
  for i in range(len(nums)):
    prod = nums[i]
    for j in range(i+1, len(nums)):
      prod = prod * nums[j]
      if prod == 1:
        if j - i + 1 > max:
          max = j - i + 1
  return max

def kadanes(arr):
  count = 0
  for i in arr:
    if i == -1:
      count += 1

  l = len(arr)
  
  if count%2==0:
    return l
  
  leftMax = 0
  for i in range(l):
    if arr[i] == -1:
      leftMax = l-i-1
      break

  rightMax = 0
  for i in range(l-1, -1, -1):
    if arr[i] == -1:
      rightMax = i
      break

  return max(leftMax, rightMax)

a = [1, -1, 1, 1, -1, -1, 1]
print(kadanes(a))

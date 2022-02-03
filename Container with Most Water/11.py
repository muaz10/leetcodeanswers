from typing import List

def maxArea(height: List[int]) -> int:
  maxA = 0
  left = 0
  right = len(height) - 1
  while left < right:
    if height[left] < height[right]:
      area = height[left] * (right - left)
      left = left + 1
    else:
      area = height[right] * (right - left)
      right = right - 1
    if area > maxA:
      maxA = area

  return maxA

height = [1,8,6,2,5,4,8,3,7]
# maxArea(height)
print(maxArea(height))
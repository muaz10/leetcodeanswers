from typing import List

def longestConsecutive(nums: List[int]) -> int:
  if len(nums) == 0:
    return 0
  sortedNums = sorted(nums)
  
  sequence = 1
  maxSequence = sequence
  initial = sortedNums[0]

  for i in range(1, len(nums)):
    if initial + 1 == sortedNums[i]:
      sequence = sequence + 1
      print(sequence)
    else:
      if sequence > maxSequence:
        maxSequence = sequence
      sequence = 1
      print(sequence)
    initial = sortedNums[i]

  if sequence > maxSequence:
    return sequence

  return maxSequence
 
 
arr = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(arr))
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

def longestConsecutive2(nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
 
class Node:
    def __init__(self, val, nex=None, prev=None):
        self.val = val
        self.next = nex
        self.prev = prev
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            mapping[i] = Node(i)
        
        for i in nums:
            if (i+1 in mapping):
                mapping[i].next = mapping[i+1]
                mapping[i+1].prev = mapping[i]
        
        ans=0
        for i in nums:
            if mapping[i].prev==None:
                curr = mapping[i]
                c=0
                while (curr):
                    curr = curr.next
                    c+=1
                ans=max(c,ans)
        return ans
 
arr = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
print(longestConsecutive(arr))
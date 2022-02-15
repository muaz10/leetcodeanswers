from typing import List

def mergeSortedIntervals(intervals: List[List[int]]) -> List[List[int]]:
  if len(intervals) < 2:
    return intervals
  intervals.sort(key=lambda x: x[0])
  ans = []
  left = intervals[0][0]
  right = intervals[0][1]
  for i in range(1, len(intervals)):
    if right >= intervals[i][0]:
      right = max(right, intervals[i][1])
    else:
      ans.append([left, right])
      left = intervals[i][0]
      right = intervals[i][1]
    if i == (len(intervals) - 1):
      ans.append([left, max(right, intervals[i][1])])
  
  return ans

  def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

intervals = [[1,4],[0,4]]
print(mergeSortedIntervals(intervals))

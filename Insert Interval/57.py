from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  intervals.append(newInterval)
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

  return inserted

intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(insert(intervals, newInterval))

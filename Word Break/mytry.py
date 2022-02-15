from typing import List
import collections

def wordBreak(s: str, wordDict: List[str]) -> bool:
  visited = set()
  que = collections.deque(s[0])

  while que:
    temp = que.popleft()
    visited.add(temp)
    if 



s = "goalspecial"
wordDict = ["go", "als", "goal", "goals", "spe", "special"]
print(wordBreak(s, wordDict))

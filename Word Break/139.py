from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
  word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

s = "goalspecial"
wordDict = ["go", "als", "goal", "goals", "spe", "special"]
print(wordBreak(s, wordDict))


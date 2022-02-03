def lengthOfLongestSubstring(s: str) -> int:
  if len(s) == 1 or len(s) == 0:
    return len(s)
  maxLen = 0
  tempMax = 0
  uni = set()
  last = 0
  for i in range(len(s)):
    if s[i] not in uni:
      tempMax += 1
      uni.add(s[i])
    else:
      if maxLen < tempMax:
        maxLen = tempMax
      j = last
      while s[j] != s[i]:
        tempMax -= 1
        uni.remove(s[j])
        j += 1
      last = j+1
      uni.add(s[i])
  if maxLen < tempMax:
    maxLen = tempMax

  return maxLen

def lengthOfLongestSubstringHashTbl(s: str) -> int:
  if len(s) == 1 or len(s) == 0:
    return len(s)
  maxLen = 0
  tempMax = 0
  dic = {}
  last = 0
  for i in range(len(s)):
    if s[i] not in dic:
      tempMax += 1
      dic[s[i]] = i
    else:
      if maxLen < tempMax:
        maxLen = tempMax
      j = last
      while s[j] != s[i]:
        tempMax -= 1
        del dic[s[j]]
        j += 1
      last = j+1
      dic[s[i]] = i
  if maxLen < tempMax:
    maxLen = tempMax

  return maxLen

s = "pwwkew"
print(lengthOfLongestSubstring(s))

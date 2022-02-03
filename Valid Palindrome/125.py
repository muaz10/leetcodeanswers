import re
def isPalindrome(s: str) -> bool:
  s = s.replace(" ", "")
  s = s.lower()
  s = re.sub(r'[^A-Za-z0-9 ]+', '', s)
  if len(s) == 0:
    return True
  l = len(s)//2
  if len(s)%2 == 1 and l != 1:
    l = l-1
  for i in range(l):
    if s[i] != s[len(s)-1-i]:
      return False
  
  return True

s = "aba"
print(isPalindrome(s))

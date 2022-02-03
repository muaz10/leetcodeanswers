def lengthOfLastWord_3(s: str) -> int:
  return len(s.split()[-1])

s = "joyboy"
print(lengthOfLastWord_3(s))

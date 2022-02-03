def lengthOfLastWord(s: str) -> int:
  replaced = s.replace(" ", ",")
  splitted = replaced.split(",")

  l = len(splitted) - 1
  last = splitted[l]
  first = splitted[0]

  while l > 0:
    if last == "":
      l=l-1
      last=splitted[l]
    else:
      return len(last)

  return len(last)

s = "joyboy"
print(lengthOfLastWord(s))

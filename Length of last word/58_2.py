def lengthOfLastWord_2(s: str) -> int:
  stri = ""
  last = False
  for i in s:
    if i != " ":
      if last == True:
        stri = i
      else:
        stri = stri + i
      last = False
    else:
      last = True

  return len(stri)

s = "joyboy"
print(lengthOfLastWord_2(s))

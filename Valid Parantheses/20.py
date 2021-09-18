def is_valid(s: str) -> bool:
  pars = []

  para_pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  for i in s:
    if i in para_pairs.values():
      pars.append(i)
    else:
      if len(pars) == 0 or para_pairs[i] != pars.pop():
        return False

  return len(pars) == 0


s = "(]"
print(is_valid(s))

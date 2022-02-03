def reverseBits(n: int) -> int:
  strn = str(n)
  if len(strn) < 32:
    for i in range(32-len(strn)):
      strn = "0" + strn
  ans = 0
  for i in range(len(strn)):
    ans = ans + (int(strn[i]) * pow(2, i))

  return ans

n = "00000010100101000001111010011100"
print(reverseBits(int(n)))
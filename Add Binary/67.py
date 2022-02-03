def addBinary(a: str, b: str) -> str:
  if a == "0":
    return b
  if b == "0":
    return a
    
  max = a
  min = b
  if len(b) > len(a):
    max = b
    min = a
  ans = ""
  bal = 0

  for i in range(len(max) - len(min)):
    min = "0" + min

  for i in range(len(max)-1, -1, -1):
    sum = int(min[i]) + int(max[i]) + bal
    if sum == 3:
      ans = "1" + ans
      bal = 1
    elif sum == 2:
      ans = "0" + ans
      bal = 1
    else:
      ans = str(sum) + ans
      bal = 0
  if bal == 1:
    return "1" + ans

  return ans

a = "10111"
b = "11010"
# addBinary(a,b)
print(addBinary(a, b))  
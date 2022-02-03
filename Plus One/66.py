from typing import List

def plusOne(digits: List[int]) -> List[int]:
  for i in range(len(digits)-1, -1, -1):
    if digits[i] + 1 < 10:
      digits[i] = digits[i] + 1
      return digits
    else:
      digits[i] = 0

  if digits[0] == 0:
    digits.insert(0, 1)

  return digits

largeInt = [8,9,9,9]
print(plusOne(largeInt))
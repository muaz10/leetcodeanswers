from typing import List

def plusOne_2(digits: List[int]) -> List[int]:
  return list(str(int(''.join(map(str, digits)))+1))

largeInt = [8,9,9,9]
print(plusOne_2(largeInt))
def maxCrossingSubarray(A, low, mid, high):
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    sum = 0
    rightSum = float('-inf')
    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > rightSum:
            rightSum = sum
            maxRight = i
    maxCrossingSum = leftSum + rightSum

    return (maxCrossingSum)


def maxSubarray(A, low, high):
    if high == low:
        return (A[low])
    else:
        mid = (low+high)//2
        return max(maxSubarray(A, low, mid),
                   maxSubarray(A, mid+1, high),
                   maxCrossingSubarray(A, low, mid, high))


def kadanes(arr):
    if len(arr) == 1:
        return arr[0]
    max = 0
    currentMax = 0
    hasZero = False
    negMax = float('-inf')
    for i in arr:
        currentMax += i
        if currentMax < 0:
            if currentMax > negMax:
                negMax = currentMax
            currentMax = 0
        elif currentMax == 0:
            hasZero = True
        if currentMax > max:
            max = currentMax

    if max == 0 and hasZero == False:
        return negMax
    else:
        return max

def kadanesOpt(arr):
  if len(arr) == 1:
      return arr[0]
  max = arr[0]
  currentMax = 0
  for i in arr:
      tempMax = currentMax + i
      if i > tempMax:
        currentMax = i
      else:
        currentMax = tempMax
      if currentMax > max:
          max = currentMax

  return max


nums = [-2, 0]
print(kadanes(nums))

def bestTimeToBuyAndSell(nums):
    d = {}
    for i in range(1, len(nums)):
        d[i] = nums[i] - nums[i-1]

    return kadanes(d)


def kadanes(arr):
    if len(arr) == 1:
        if arr[1] > 0:
            return arr[1]
        else:
            return 0
    max = 0
    currentMax = 0
    for i in arr:
        if arr[i] > 0:
            currentMax += arr[i]
            if currentMax < 0:
                currentMax = 0
            if currentMax > max:
                max = currentMax

    return max


def bestTimeToBuyAndSell2(nums):
    sum = 0
    for i in range(1, len(nums)):
        d = nums[i] - nums[i-1]
        if d > 0:
            sum += d
    return sum


arr = [7, 6, 4, 3, 1]
print(bestTimeToBuyAndSell2(arr))

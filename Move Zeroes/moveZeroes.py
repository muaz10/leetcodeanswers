def moveZeroes(nums):
    j = len(nums)
    for i in range(j-1, -1, -1):
        if nums[i] == 0:
            j -= 1
            if i != j:
                for k in range(i, j):
                    temp = nums[k]
                    nums[k] = nums[k+1]
                    nums[k+1] = temp
    return nums


def moveZeroes2(nums):
    j = len(nums)
    d = {}
    for i in range(j-1, -1, -1):
        if nums[i] == 0:
            j -= 1
            if j != i:
                nums[i] = nums[j]
                nums[j] = 0
        else:
            d[i] = nums[i]
    for i in d:
        j -= 1
        nums[j] = d[i]

    return nums


def moveZeroes3(nums):
    j = 0
    for i in nums:
        if i != 0:
            nums[j] = i
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0

    return nums


def moveZeroes4(nums):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            nums[i] = 0
            j += 1
    return nums


arr = [0, 1, 0, 12, 2]
print(moveZeroes4(arr))

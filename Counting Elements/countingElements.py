def countingElements(nums):
    count = 0
    l = len(nums)
    d = {}
    for i in range(l):
        d[i] = nums[i]
    for i in d:
        if d[i]+1 in d.values():
            count += 1

    return count


arr = [1, 1, 2, 2]
print(countingElements(arr))

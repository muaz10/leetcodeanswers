def findShortestSubArray(self, nums: List[int]) -> int:
    dic = {}
    indexes = {}
    maxi = nums[0]
    maxies = [nums[0]]
    
    for i in range(len(nums)):
        if nums[i] in dic:
            dic[nums[i]] += 1
            indexes[nums[i]].append(i)
        else:
            dic[nums[i]] = 1
            indexes[nums[i]] = [i]
            
        if dic[maxi] < dic[nums[i]] or maxi == nums[i]:
            maxi = nums[i]
            maxies = [nums[i]]
        elif maxi != nums[i] and dic[maxi] == dic[nums[i]]:
            maxi = nums[i]
            maxies.append(nums[i])
        
            
            
    if len(maxies) == 1:
        return indexes[maxi][-1] - indexes[maxi][0] + 1
    ans = []
    for i in maxies:
        ans.append(indexes[i][-1] - indexes[i][0] + 1)
        
    return min(ans)
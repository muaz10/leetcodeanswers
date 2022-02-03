def getServedBuildings(buildingCount, routerLocation, routerRange):
    # Write your code here
    n = len(buildingCount)
    ans = 0
    for i in range(len(routerLocation)):
        baseLoc = routerLocation[i] - 1
        ran = routerRange[i]
        buildingCount[baseLoc] -= 1
        for j in range(1, ran+1):
            left = baseLoc - j
            right = baseLoc + j
            
            if left < 0 and right > n:
                break
            if left >= 0:
                buildingCount[left] -= 1
            if right < n:
                buildingCount[right] -= 1
            
    for i in range(n):
        if buildingCount[i] <= 0:
            ans += 1
    
    return ans

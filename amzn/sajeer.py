from math import ceil
def findEarliestMonth(stocks):
    leftsum = stocks[0]
    left = 1
    rightsum = 0
    right = len(stocks)-1
    for i in range(1, len(stocks)):
        rightsum += stocks[i]

    avgsarr = [abs(leftsum-(rightsum//right))]
    for i in range(1, len(stocks)-1):
        left += 1
        right -= 1
        leftsum += stocks[i]
        rightsum -= stocks[i]
        avgsarr.append(abs((leftsum//left)-(rightsum//right)))

    minchange = float('inf')
    minindex = -1
    for i in range(len(avgsarr)):
        if avgsarr[i] < minchange:
            minchange = avgsarr[i]
            minindex = i+1

    return minindex

stocks = [1, 3, 2, 3]
# print(findEarliestMonth(stocks))

def CountSwap(s):
    s = list(s)
    count = 0
    ans = True
    n = len(s)
 
    for i in range(n // 2):
 
        left = i
        right = n - left - 1
 
        while left < right:
            if s[left] == s[right]:
                break
            else:
                right -= 1
 
        if left == right:
            ans = False
            break
        else:
            for j in range(right, n - left - 1):
                (s[j], s[j + 1]) = (s[j + 1], s[j])
                count += 1
    if ans:
        return (count)
    else:
        return -1

def misSwap(s):
    ans1 = CountSwap(s)
    ans2 = CountSwap(s[::-1])
    print(ans1)
    print(ans2)
    return min(ans1, ans2)

def solution(s):
    l=0
    r=len(s)-1
    ans=0
    while (l<r):
        if s[l]!=s[r]:
            ans+=1
        l+=1
        r-=1
    if len(s)%2==0:
        if ans%2==1:
            return -1
    return ceil(ans/2)


s = "0100101"
print(solution(s))
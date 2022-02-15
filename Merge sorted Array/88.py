from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    mi = 0
    ni = 0
    i = 0
    ans = []

    for j in range(m):
        ans.append(nums1[j]) 

    while mi < m and ni < n:
        if ans[mi] <= nums2[ni]:
            nums1[i] = ans[mi]
            mi += 1
        else:
            nums1[i] = nums2[ni]
            ni += 1
        i += 1
        
    while mi < m:
        nums1[i] = ans[mi]
        mi += 1
        i += 1

    while ni < n:
        nums1[i] = nums2[ni]
        ni += 1
        i += 1
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)

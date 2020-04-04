Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

There are two approaches. One is using the divide and conquer method. We divide the array into two using the mid point. Then find the maximum subarray
of the left, right and the one which contains the mid point. The left and right are sub problems of the main one. For the other one we find the max
sum from mid to left and from mid to right and merge them. Finally return the maximum of those three.

Second way is using dynamic programming greedy approach


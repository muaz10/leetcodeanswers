Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

The usual approach would be using two iterations. But this will consume lot of time. It took 5568 ms and 12.4 mb memory for 29 test cases.
But if you use a dictionary based search, the time will be reduced drastically. It took just 32 ms for 29 test cases.

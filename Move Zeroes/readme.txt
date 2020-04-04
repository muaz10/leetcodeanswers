Problem: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

First it's a brute force approach, you iterate through the array, if you find a zero, then move it to the last position, again iterating one 
by one. So the time complexity is O(n^2). The second way, you just swap the zero with the element in the last position(have a pointer and reduce
it everytime you swap) and store the swapped one in a hash table. Then use the pointer to iterate through remaining elements which are non zero
and replace with the ones in the hash table. It will restore the order. 
Other two approaches are, bring each non zero element(have a pointer to save the last non zero element) and make all the other elements after the
pointer 0. All 3 approaches has O(n) time complexity. However the final one is the optimal because it needs to go through only the non zero 
elements. 

Problem: Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

First approach is a horizontal search. We search through the elements in the array, one after
the other. 
Second method is a vertical search. Check the elements of each string in a given index in one
iteration.
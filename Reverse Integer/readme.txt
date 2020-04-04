Problem: Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

The first approach is without converting it into string. We have to convert it into a positive integer anyway because, you can't use 
modulus operator to negative numbers to get remainder unlike in java or C++, and also division operator gives floor function output.

Second method is by converting into string. Using slicing, you can easily get the reverse of string. There are two ways using string,
one is slicing according to its sign. Second way is to get the absolute value and then return the reversed integer according to the 
input's sign.
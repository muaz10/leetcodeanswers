Problem: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

First we will conver it into string. It is a two line code.
Next, without converting into string. Obviously, negattive numbers and numbers which end with 0 which are not 0 are not palindrome.
So return false for those. Then convert half of the input and check if it is matching with the input(convert until the converted number is
greater than the input).
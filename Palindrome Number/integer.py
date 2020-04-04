class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        if x < 0 or x%10 == 0 and x != 0:
            return False
        while x > rev:
            rev = rev*10 + x%10
            x = x//10
        if rev == x or rev//10 == x:
            return True
        else:
            return False
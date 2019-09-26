class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x < 0:
            y = -x
        else:
            y = x

        while y != 0:
            pop = y % 10
            y = y // 10
            if rev > 214748364 or rev == 214748364 and pop > 7:
                return 0        
            if rev < -214748364 or rev == -214748364 and pop < -8:
                return  0
            rev = rev * 10 + pop
        
        if x < 0:
            return -rev
        else:
            return  rev
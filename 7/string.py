class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:    
            a =  int(str(x)[::-1])  
        if x <=0:    
            a = -int(str(x)[:0:-1])
      
        mina = -2**31  
        maxa = 2**31 - 1  
        if a not in range(mina, maxa):  
            return 0  
        else:  
            return a

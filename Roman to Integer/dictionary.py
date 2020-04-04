class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        i = 0
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        while i < len(s):
            if i == len(s)-1:
                integer += romans[s[i]]
                break

            sym = romans[s[i]]
            nexSym = romans[s[i+1]]
            if sym < nexSym:
                integer += nexSym - sym
                i += 2
            else:
                integer += sym
                i += 1        
        return integer
            
            
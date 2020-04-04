class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        i = 0
        while i < len(s):      
            if s[i] == "V":
                integer += 5
                i += 1
            elif s[i] == "L":
                integer += 50
                i += 1
            elif s[i] == "D":
                integer += 500
                i += 1
            elif s[i] == "M":
                integer += 1000
                i += 1        
            elif s[i] == "I":
                if i == len(s)-1:
                    integer += 1
                    i += 1
                elif s[i+1] == "V":
                    integer += 4
                    i += 2
                elif s[i+1] == "X":
                    integer += 9
                    i += 2
                else:
                    integer += 1
                    i += 1
            elif s[i] == "X":
                if i == len(s)-1:
                    integer += 10
                    i += 1
                elif s[i+1] == "L":
                    integer += 40
                    i += 2
                elif s[i+1] == "C":
                    integer += 90
                    i += 2
                else:
                    integer += 10
                    i += 1
            elif s[i] == "C":
                if i == len(s)-1:
                    integer += 100
                    i += 1
                elif s[i+1] == "D":
                    integer += 400
                    i += 2
                elif s[i+1] == "M":
                    integer += 900
                    i += 2
                else:
                    integer += 100
                    i += 1        
        return integer
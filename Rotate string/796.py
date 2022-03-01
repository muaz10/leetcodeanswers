def rotateStringBruteForce(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            if s == goal:
                return True
            else:
                temp = s[0]
                s = s[1:]
                s += temp
                
        return False

def rotateString2(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        rem = ""
        while len(s) > 0:
            res = goal.find(s)
            if res == -1:
                rem = s[-1] + rem
                s = s[:-1]
            else:
                if res == 0 and len(rem) == 0:
                    return True
                if goal[0:res] == rem:
                    return True
                else:
                    return False
                
        return False

def rotateString3(self, s: str, goal: str) -> bool:
        s1=s[0]
        
        s2=""
        for i in range(len(goal)):
            if s1==goal[i]:
                if goal[i:]==s[:len(goal)-i] and goal[:i]==s[len(goal)-i:]:
                    return True
        return False
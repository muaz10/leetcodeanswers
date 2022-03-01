from typing import List

def letterCombinations(digits: str) -> List[str]:
    numlets = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
    l = len(digits)
    if l == 0:
        return []
    
    letlist = []
    for i in digits:
        letlist.append(numlets[i])
    
    if l == 1:
        return letlist[0]
    ans = []
    if l == 2:
        for i in letlist[0]:
            for j in letlist[1]:
                ans.append(i+j)
        return ans

    if l == 3:
        for i in letlist[0]:
            for j in letlist[1]:
                for k in letlist[2]:
                    ans.append(i+j+k)
        return ans

    if l == 4:
        for i in letlist[0]:
            for j in letlist[1]:
                for k in letlist[2]:
                    for m in letlist[3]:
                        ans.append(i+j+k+m)
        return ans

    def letterCombinationsDFS(digits: str) -> List[str]:
        numlets = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        if digits == "":
            return []
        def dfs(s, ans):
            if s=="":
                return ans
            c=s[0]
            newAns = []
            for i in numlets[c]:
                for cs in ans:
                    newAns.append(cs+i)
            return dfs(s[1:], newAns)
        
        return dfs(digits,[""])


digits = "23"
print(letterCombinations(digits))
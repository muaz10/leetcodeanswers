from typing import List

def longestPalindrome(self, s: str) -> int:
    if len(s) == 0:
        return 0
    dic = set()
    ans = ""
    for i in s:
        if i in dic:
            ans = ans + i
            dic.remove(i)
        else:
            dic.add(i)

    l = len(ans)

    if len(dic) > 0:
        return l + l + 1
    else:
        return l + l

    
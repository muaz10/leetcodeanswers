from typing import List

def reverseString(s: List[str]) -> None:
    l = len(s) - 1
    for i in range(l//2+1):
        temp = s[i]
        s[i] = s[l-i]
        s[l-i] = temp 

    print(s)

s = ["T","h","o","m","a", "s"]
reverseString(s)

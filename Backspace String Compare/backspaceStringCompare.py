def backspaceStringCompare(S, T):
    if len(S) == 1 and len(T) == 1:
        return S == T
    str1 = ""
    str2 = ""
    for i in S:
        if i == '#':
            str1 = str1[:-1]
        else:
            str1 = str1 + i
    for i in T:
        if i == '#':
            str2 = str2[:-1]
        else:
            str2 = str2 + i

    return str1 == str2


S = "a#c"
T = "b"
print(backspaceStringCompare(S, T))
# print(T[:-1])

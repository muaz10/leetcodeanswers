def decodeString(s: str) -> str:
    stack = []
    numint = 0
    decode = ""
    ans = ""

    for i in s:
        if i.isdigit():
            numint = numint * 10 + int(i)
        elif i == "[":
            stack.append(numint)
            stack.append("[")
            numint = 0
        elif i.isalpha():
            stack.append(i)
        elif i == "]":
            while stack[-1] != "[":
                decode = stack.pop() + decode
            stack.pop()
            k = stack.pop()
            decode = decode * k
            for j in decode:
                stack.append(j)
            decode = ""

    return ''.join(stack)


s = "2[abc]3[cd]ef"
print(decodeString(s))

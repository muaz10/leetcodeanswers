def reverse(x):
    if x > 0:  # handle positive numbers  
        a =  int(str(x)[::-1])  
    if x <=0:  # handle negative numbers  
        a = -int(str(x)[:0:-1])
    # handle 32 bit overflow  
    mina = -2**31  
    maxa = 2**31 - 1  
    if a not in range(mina, maxa):  
        return 0  
    else:  
        return a


print(reverse(-12348098))

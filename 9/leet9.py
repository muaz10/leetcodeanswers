def palindrome(x):
    y = x
    rev = 0
    while y > 0:
        pop = y%10
        y = y//10
        rev = rev*10 + pop
        print(rev)
    if rev == x:
        return True
    else:
       return False


print(palindrome(1223221))

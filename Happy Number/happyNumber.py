def happyNumber(num):
    if num == 1 or num == 7:
        return True
    while len(str(num)) != 1:
        sum = 0
        for i in  str(num):
            sum += int(i) * int(i)
        num = sum
    return num == 1 or num == 7

num = 19
print(happyNumber(num))
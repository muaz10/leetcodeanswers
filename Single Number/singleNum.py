def singleNumber(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] = 2
        else:
            dict[i] = 1
    
    for i in list:
        if dict[i] == 1:
            return i

list = [4,1,2,1,2,4,5]
print(singleNumber(list))
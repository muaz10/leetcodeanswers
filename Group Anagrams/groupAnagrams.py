def groupAnagrams(strs):
    l = len(strs)
    res = []
    added = []
    empty = []
    for i in range(l):
        item = strs[i]
        if item == "":
            empty.append(item)
        else:
            if item not in added:
                occurs = {}
                for k in item:
                    occurs[k] = item.count(k)
                ana = []
                ana.append(item)
                for j in range(i+1, l):
                    item2 = strs[j]
                    if len(item) == len(item2):
                        flag = True
                        for k in item:
                            if k not in item2:
                                flag = False
                                break
                            elif occurs[k] != item2.count(k):
                                flag = False
                                break
                        if flag == True:
                            ana.append(item2)
                            added.append(item2)
                res.append(ana)

    if len(empty) != 0:
        res.append(empty)
    return res


def groupAnagrams2(strs):
    res = {}
    empty = []
    for i in strs:
        if i == "":
            empty.append("")
        else:
            dic = [0] * 26
            for j in i:
                dic[ord(j)-97] += 1
            if tuple(dic) in res:
                res[tuple(dic)].append(i)
            else:
                res[tuple(dic)] = [i]

    if len(empty) != 0:
        res['empty'] = empty

    ans = []
    for i in res:
        ans.append(res[i])

    return ans


arr = ["", "t", "tan", "ate", "nat", "bat", "tat", "tata"]
print(groupAnagrams2(arr))
# print(ord('a'))

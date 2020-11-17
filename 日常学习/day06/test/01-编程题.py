# 元素分类 有如下值集合
# [11,22,33,44,55,66,77,88,99,90]，将所有⼤于66 的值保存
# ⾄字典的第⼀个key对应的值中，将⼩于66 的值保存⾄第
# ⼆个key 对应的值中。
iDict = {"key1": [], "key2":[]}
iList = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
for iNum in iList:
    if iNum > 66:
        iDict["key1"].append(iNum)
    elif iNum < 66:
        iDict["key2"].append(iNum)

print(iDict)
# 统计字符串中字符出现的次数，如果是空格，不
# 输出。
#  如："hello world" 字符串统计的结果为：{'l': 3, 'h':
# 1, 'w': 1, 'd': 1, 'o': 2, 'r': 1, 'e': 1}

iDict = {}
iString = "hello world"
for iStr in iString:
    if iStr not in iDict:
        iDict[iStr] = 1
    else:
        iDict[iStr] += 1
print(iDict)

# 快速排序

from randomList import randomList

iList = randomList(20)


def quickSort(iList):
    if len(iList) <= 1:
        return iList
    left = []
    right = []
    for i in iList[1:]:
        if i <= iList[0]:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [iList[0]] + quickSort(right)

# def quickSort(iList):
#     if len(iList) <= 1:
#         return iList
#
#     left = []
#     right = []
#     for i in iList[1:]:
#         if i <= iList[0]:
#             left.append(i)
#         else:
#             right.append(i)
#     return quickSort(left) + [iList[0]] + quickSort(right)
#
#
# if __name__ == "__main__":
#     print(iList)
#     print(quickSort(iList))

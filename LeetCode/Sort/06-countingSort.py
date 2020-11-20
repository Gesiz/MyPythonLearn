from randomList import randomList

iList = randomList(20)


def countingSort(iList):
    ilen = len(iList)
    if ilen <= 1:
        return iList

    mList = [None] * ilen
    for i in range(ilen):
        same = 0
        small = 0
        for j in range(ilen):
            if iList[i] > iList[j]:
                small += 1
            if iList[i] == iList[j]:
                same += 1

        for k in range(small, small + same):
            mList[k] = iList[i]

    return mList


# def countingSort(iList):
#     if len(iList)<1:
#         return iList
#     ilen = len(iList)
#     rList = [None] * ilen
#     for i in range(ilen):
#         small = 0
#         same = 0
#         for j in range(ilen):
#             if iList[i] > iList[j]:
#                 small += 1
#             if iList[i] == iList[j]:
#                 same += 1
#         for k in range(small,small+same):
#             rList[k] = rList[i]
#     return iList

# def countingSort(iList):
#     if len(iList) <= 1:
#         return iList
#     iLen = len(iList)
#     rList = [None] * iLen
#     for i in range(iLen):
#         small = 0
#         same = 0
#         for j in range(iLen):
#             if iList[j] < iList[i]:
#                 small += 1
#             elif iList[j] == iList[i]:
#                 same += 1
#         for k in range(small, small + same):
#             rList[k] = iList[i]
#     return rList
# 
# 
if __name__ == "__main__":
    print(iList)
    print(countingSort(iList))

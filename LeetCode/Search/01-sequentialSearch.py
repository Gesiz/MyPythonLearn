import LeetCode.Sort.randomList as randomList
import LeetCode.Sort.quickSort as quickSort

import random

iList = randomList.randomList(20)
iList = quickSort.quickSort(iList)



def sequentialSearch(iList, key):
    print("iList=%s" % str(iList))
    print("Find The number %d" % key)
    iLen = len(iList)
    for i in range(iLen):
        if iList[i] == key:
            return i
    else:
        return -1




    # iLen = len(iList)
    # for i in range(iLen):
    #     if iList[i] == key:
    #         return i
    # return -1


if __name__ == "__main__":
    keys = [random.choice(iList), random.randrange(min(iList), max(iList))]
    for key in keys:
        res = sequentialSearch(iList, key)
        if res >= 0:
            print(f"{key}is in the list index is : {res}")
        else:
            print(f"{key} is not in the list")


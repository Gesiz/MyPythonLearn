from LeetCode.Sort.randomList import randomList
from LeetCode.Sort.quickSort import quickSort
import random

iList = quickSort(randomList(20))


def binarySearch(iList, key):
    print(f"iList = {iList}")
    print(f"find the number{key}")

    iLen = len(iList)
    left = 0
    right = iLen - 1

    while right - left > 1:
        mid = (right + left) // 2

        if key > iList[mid]:
            left = mid

        elif key < iList[mid]:
            right = mid

        else:
            return mid











    # iLen = len(iList)
    # left = 0
    # right = iLen - 1
    #
    # while right - left > 1:
    #     mid = (left + right) // 2

    #     if key < iList[mid]:
    #         right = mid
    #     elif key > iList[mid]:
    #         left = mid
    #     else:
    #         return mid
    #
    #     if key == iList[left]:
    #         return left
    #
    #     elif key == iList[right]:
    #         return right
    #     else:
    #         return -1


if __name__ == "__main__":
    keys = [random.choice(iList), random.randrange(min(iList), max(iList))]
    for key in keys:
        res = binarySearch(iList, key)
        if lex >= 0:
            print(f"{key} is in the list , index is {res}")
        else:
            print(f"{key} is not in the list")

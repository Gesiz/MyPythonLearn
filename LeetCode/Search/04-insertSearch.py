from LeetCode.Sort.randomList import randomList
from LeetCode.Sort.quickSort import quickSort
import random

iList = quickSort(randomList(20))


def insertSearch(iList, key):
    print(f"iList = {iList}")
    print(f"Find The number : {key}")
    iLen = len(iList)
    left = 0
    right = 0

    while right - left > 1:
        mid = left + (key - iList[left]) * (right - left) // (iList[right] - iList[left])

        if mid == left:
            mid += 1

        if key < iList[mid]:
            right = mid
        elif key > iList[mid]:
            left = mid
        else:
            return mid
    if key == iList[left]:
        return left
    elif key == iList[right]:
        return right
    else:
        return -1


if __name__ == "__main__":
    keys = [random.choice(iList), random.randrange(min(iList), max(iList))]
    for key in keys:
        res = insertSearch(iList, key)
        if res >= 0:
            print(f"{key} is in the list , index is {res}")
        else:
            print(f"{key} is not in the list")
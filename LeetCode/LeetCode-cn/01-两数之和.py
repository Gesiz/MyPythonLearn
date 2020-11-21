class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        iDict = {}
        for i, j in enumerate(nums):
            iDict[j] = i

        for i, j in enumerate(nums):

            k = iDict.get(target - j)
            if k is not None and k != i:
                return [i, k]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        iDict = {}
        for i, j in enumerate(nums):
            if iDict.get(target - j) is not None:
                return [iDict.get(target - j), i]

            iDict[j] = i

Solution.twoSum(None,[2,7,11,15],9)
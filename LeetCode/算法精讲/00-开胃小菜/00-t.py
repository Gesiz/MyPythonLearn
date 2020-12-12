


class Solution:
    def minSubArrayLen(self,s:int,nums:list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1

        start = end = 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans






























# class Solution:
#     def binarySearch(self, iList, target):
#         l, r = 0, len(iList) - 1
#         while r >= l:
#             mid = (l+r) // 2
#             if target == iList[mid]:
#                 return mid
#             elif target > iList[mid]:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#             # elif target < iList[mid]:
#             #     r = mid - 1
#             # else:
#             #     l = mid + 1
#         return l
#
#
# A = Solution()
# print(A.binarySearch([1, 2, 3, 4, 5, 6, 7], 9))

#
# def fib(N):
#     if N <= 2:
#         return N
#     return fib(N-1) + fib(N-2)
# print(fib(3))

class Solution:
    def binarySearch(self,nums, target):
        if len(nums) <= 1:
            return nums

        l = 0
        r = len(nums) -1

        while r - l >= 0:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


A = Solution()
print(A.binarySearch([1, 2, 3, 4, 5], 4))

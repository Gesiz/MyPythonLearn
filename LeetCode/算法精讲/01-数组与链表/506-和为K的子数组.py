# class Soluction:
#     def subarraySum(self,nums,k):
#         ilen = len(nums)
#         result = 0
#         presum = [None] * (ilen + 1)
#
#         sum = 0
#
#         for i in range(ilen):
#             presum[i] = sum
#             sum += nums[i]
#
#         presum[ilen] = sum
#
#         for i in range(ilen + 1):
#             j = i+1
#             for j in range(ilen + 1):
#                 if presum[j] - presum[i] == k:
#                     result +=1
#         return result
#
# A = Soluction()
# print(A.subarraySum([1,1,1],0))
#
class Solution:
    def subarrySum(self,nums,k:int)->int:
        import collections
        num_times = collections.defaultdict(int)
        num_times[0] = 1
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in num_times:
                res += num_times[cur_sum - k]
            num_times[cur_sum] += 1
        return res

s = Solution()
print(s.subarrySum([1,1,1],0))
# import collections
# num_times = collections.defaultdict(int)
# nums = dict()
# print(nums.get('key',0))
# print(num_times['key'])
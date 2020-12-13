# class Solution:
#
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         return self.fib(N - 1) + self.fib(N - 2)
#
#

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


A = Solution()
print(A.numWays(0))
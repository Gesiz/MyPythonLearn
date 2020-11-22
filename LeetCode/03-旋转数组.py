# 给定一个数组 将数组中的元素向右移动k个位置 其中k是非负数

class Solution:
    def rotate(self, nums, k):
        if len(nums) < 2:
            return
        nums.reverse()

        k = k % len(nums)  # 避免k大于nums的长度
        while k > 0:
            temp = nums.pop(0)
            nums.append(temp)
            k -= 1
        nums.reverse()
        return

#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count], nums[i] = nums[i], 0
        print(nums)

# @lc code=end

s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
s.moveZeroes([0])

#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
from typing import List

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mmax = nums[0]
        isFirst = True
        first_idx = 0
        last_idx = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num >= mmax:
                mmax = num
            else:
                if isFirst:
                    isFirst = False
                    first_idx = i - 1
                last_idx = i + 1
        return last_idx - first_idx


# @lc code=end
s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1]))
print(s.findUnsortedSubarray([1, 2]))
print(s.findUnsortedSubarray([2, 1]))
print(s.findUnsortedSubarray([5, 4, 3, 2, 1]))
print(s.findUnsortedSubarray([1, 2, 3, 3, 3]))
print(s.findUnsortedSubarray([2, 3, 3, 2, 4]))


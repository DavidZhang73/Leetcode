#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        mmax = -float("INF")
        for num in nums:
            pre = max(pre + num, num)
            mmax = max(mmax, pre)
        return mmax


# @lc code=end
s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

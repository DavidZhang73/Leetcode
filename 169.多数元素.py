#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        target = int(len(nums) / 2)
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
            if m[num] > target:
                return num
# @lc code=end
s = Solution()
print(s.majorityElement([3,2,3]), 3)
print(s.majorityElement([2,2,1,1,1,2,2]), 2)

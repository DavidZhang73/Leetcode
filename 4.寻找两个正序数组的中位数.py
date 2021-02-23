#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # left = 0
        # right = 0
        # num_list = []
        # while left < len(nums1) and right < len(nums2):
        #     if nums1[left] <= nums2[right]:
        #         num_list.append(nums1[left])
        #         left += 1
        #     else:
        #         num_list.append(nums2[right])
        #         right += 1
        # while left < len(nums1):
        #     num_list.append(nums1[left])
        #     left += 1
        # while right < len(nums2):
        #     num_list.append(nums2[right])
        #     right += 1
        num_list = sorted(nums1 + nums2)
        l = len(nums1) + len(nums2)
        is_odd = l % 2 != 0
        if is_odd:
            return num_list[int(l / 2)]
        else:
            return (num_list[int(l / 2) - 1] + num_list[int(l / 2)]) / 2


# @lc code=end

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))


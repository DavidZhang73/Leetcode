#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        p = l1
        times = 1
        while p:
            s += p.val * times
            times *= 10
            p = p.next
        p = l2
        times = 1
        while p:
            s += p.val * times
            times *= 10
            p = p.next
        nums = str(s)[::-1]
        ret = ListNode(int(nums[0]))
        p = ret
        for num in nums[1:]:
            p.next = ListNode()
            p = p.next
            p.val = int(num)
        return ret


# @lc code=end


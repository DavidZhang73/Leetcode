#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ret = -int(str(x)[1:][::-1])
        elif x > 0:
            ret = int(str(x)[::-1])
        else:
            return 0
        INT_MIN = -(2 ** 31)
        INT_MAX = -INT_MIN - 1
        if ret <= INT_MIN or ret >= INT_MAX:
            return 0
        else:
            return ret


# @lc code=end
s = Solution()
print(s.reverse(123), 321)
print(s.reverse(-123), -321)
print(s.reverse(120), 21)

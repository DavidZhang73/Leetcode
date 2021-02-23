#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

import re

# @lc code=start
class Solution:
    INT_MIN = -(2 ** 31)
    INT_MAX = -INT_MIN - 1

    def isNumber(self, char: str) -> bool:
        return ord(char) >= ord("0") and ord(char) <= ord("9")

    def myAtoi(self, str: str) -> int:
        isPositive = True
        str = str.strip()
        if str == "":
            return 0
        first = str[0]
        if first == "+":
            str = str[1:]
        elif first == "-":
            str = str[1:]
            isPositive = False
        elif not self.isNumber(first):
            return 0
        ret = 0
        for num in str:
            if self.isNumber(num):
                ret = ret * 10 + int(num)
            else:
                break
        ret *= 1 if isPositive else -1
        if ret < self.INT_MIN:
            return self.INT_MIN
        elif ret > self.INT_MAX:
            return self.INT_MAX
        else:
            return ret


# @lc code=end

s = Solution()
for case in [
    ["42", 42],
    ["   -42", -42],
    ["4193 with words", 4193],
    ["words and 987", 0],
    ["", 0],
    ["-91283472332", -2147483648],
    ["3.14159", 3],
    ["-", 0],
    ["+1", 1],
    ["+", 0],
    [" ", 0],
]:
    result = s.myAtoi(case[0])
    print("test case:", result, case[1])
    assert result == case[1]

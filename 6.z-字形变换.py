#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1:
            return s
        ret = []
        locate_list = []
        # first line
        for i in range(0, len(s), 2 * (numRows - 1)):
            locate_list.append(i)
            ret.append(s[i])
        # middle lines
        locate_list.append(i + 2 * (numRows - 1))
        for l in range(1, numRows - 1):
            for locate in locate_list:
                if locate - l > 0 and locate - l < len(s):
                    ret.append(s[locate - l])
                if locate + l < len(s):
                    ret.append(s[locate + l])
        # last line
        for i in range(numRows - 1, len(s), 2 * (numRows - 1)):
            ret.append(s[i])
        return "".join(ret)


# @lc code=end

s = Solution()
assert s.convert(s="A", numRows=1) == "A"
assert s.convert(s="LEETCODEISHIRING", numRows=3) == "LCIRETOESIIGEDHN"
assert s.convert(s="LEETCODEISHIRING", numRows=4) == "LDREOEIIECIHNTSG"


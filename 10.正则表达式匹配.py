#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

import re

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(rf"^{p}$", s) != None


# @lc code=end

s = Solution()
print(s.isMatch("aa", "a"), False)
print(s.isMatch("aa", "a*"), True)
print(s.isMatch("ab", ".*"), True)
print(s.isMatch("aab", "c*a*b"), True)
print(s.isMatch("mississippi", "mis*is*p*."), False)

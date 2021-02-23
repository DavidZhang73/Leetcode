#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ret = s[0]
        max_len = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    if len(sub) > max_len:
                        ret = sub
                        max_len = len(sub)
        return ret


# @lc code=end

s = Solution()
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome(""))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))

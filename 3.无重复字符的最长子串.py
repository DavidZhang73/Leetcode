#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ret = 1
        m = {s[0]: 0}
        left = 0
        for right in range(1, len(s)):
            old_position = m.get(s[right], -1)
            if old_position != -1:
                for i in range(left, old_position + 1):
                    del m[s[i]]
                left = old_position + 1
                print('yes', left, right)
            else:
                ret = max(right - left + 1, ret)
                print('yes', left, right)
            m[s[right]] = right
        return ret


# @lc code=end

s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))

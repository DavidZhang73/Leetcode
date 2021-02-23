#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    dp = [0, 1] + [-1] * 29

    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        elif self.dp[N - 1] != -1:
            self.dp[N] = self.dp[N - 2] + self.dp[N - 1]
            return self.dp[N]
        else:
            return self.fib(N - 1) + self.fib(N - 2)


# @lc code=end
s = Solution()
print(s.fib(2), 1)
print(s.fib(3), 2)
print(s.fib(4), 3)
print(s.fib(30), 3)

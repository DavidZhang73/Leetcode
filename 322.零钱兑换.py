#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # mem = {}
        # def dp(amount):
        #     if amount in mem:
        #         return mem[amount]
        #     if amount < 0:
        #         return -1
        #     if amount == 0:
        #         return 0
        #     ret = float('INF')
        #     for coin in coins:
        #         subproblem = dp(amount - coin)
        #         if subproblem == -1:
        #             continue
        #         ret = min(ret, subproblem + 1)
        #     mem[amount] = ret if ret != float('INF') else -1
        #     return mem[amount]
        # return dp(amount)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]


# @lc code=end

s = Solution()
print(s.coinChange([1, 2, 5], 11), 3)
print(s.coinChange([2], 3), -1)

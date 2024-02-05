class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)

        # Initialize hold and cash arrays
        hold = [0] * n
        cash = [0] * n

        # Initialize the first day's hold and cash values
        hold[0] = -prices[0]
        cash[0] = 0

        for i in range(1, n):
            # Update hold and cash values based on the recurrence relations
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i] - fee)

        # The maximum profit is the maximum of the last day's hold and cash values
        return max(hold[-1], cash[-1])

# Example usage:
solution = Solution()
print(solution.maxProfit([1,3,2,8,4,9], 2))
print(solution.maxProfit([1,3,7,5,10,3], 3))

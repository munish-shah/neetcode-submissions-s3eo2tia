class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0
        max_profit = 0
        for i in prices:
            if i < low:
                low = i
                high = i
            if i > high:
                high = i

            if high - low > 0 and high - low > max_profit:
                max_profit = high - low
        return max_profit



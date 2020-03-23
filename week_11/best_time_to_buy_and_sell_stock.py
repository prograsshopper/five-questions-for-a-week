# worst : O(N^2) 5.01%
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         output_arr = []
#         for i in range(0, len(prices)-1):
#             max_num = max(prices[i:])
#             output_arr.append(max_num - prices[i])
#         return max(output_arr) if output_arr else 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def rec(lst: List[int]) -> (int, int): # best trade so far, lowest so far
            if len(lst) == 1:
                return (0, lst[0])
            best_trade, lowest = rec(lst[:-1])
            last = lst[-1]

            if last-lowest > best_trade:
                best_trade = last-lowest

            if last < lowest:
                lowest = last
            
            return (best_trade, lowest)
        
        best, _ = rec(prices)
        return best
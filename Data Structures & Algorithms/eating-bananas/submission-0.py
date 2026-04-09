class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        res = end
        
        while start <= end:
            k = (start + end) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x / k)

            if hours <= h:
                res = min(res, k)
                end = k - 1
            else:
                start = k + 1
        
        return res
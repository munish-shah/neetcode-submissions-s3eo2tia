class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for num, freq in frequency.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
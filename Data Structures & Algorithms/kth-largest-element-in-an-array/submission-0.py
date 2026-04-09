class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for x in nums:
            maxHeap.append(-1 * x)
        
        heapq.heapify(maxHeap)
        while k > 0:
            k -= 1
            num = heapq.heappop(maxHeap)
            if k == 0:
                return -1 * num
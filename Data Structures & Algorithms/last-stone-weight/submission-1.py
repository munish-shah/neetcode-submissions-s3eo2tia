class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-x for x in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            y = heapq.heappop(minHeap)
            x = heapq.heappop(minHeap)
            if x != y:
                heapq.heappush(minHeap, (y - x))
    
        minHeap.append(0)
        return abs(minHeap[0])


        

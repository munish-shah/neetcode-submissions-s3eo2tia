class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_size = 0
        # for x in range(len(heights) - 1):

        while left < right:
            distance = right - left
            curr_size = min(heights[left], heights[right]) * distance
            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
            max_size = max(curr_size, max_size)
        return max_size
            
            
            

            

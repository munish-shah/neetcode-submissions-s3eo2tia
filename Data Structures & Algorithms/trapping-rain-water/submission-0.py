class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        total_water = 0
    
        while l < r:
            
            if maxRight <= maxLeft:
                r -=1
                if maxRight - height[r] > 0:
                    total_water += maxRight - height[r]
                else:
                    maxRight = height[r]
            elif maxLeft < maxRight:
                l += 1
                if maxLeft - height[l] > 0:
                    total_water += maxLeft - height[l]
                else:
                    maxLeft = height[l]
        
        return total_water
                
            

        
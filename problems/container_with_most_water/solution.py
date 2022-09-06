class Solution:
    """To be effiencient try using 2 pointers, one that starts at the left and one at the right"""
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0 
        max_area = 0
        while l < r:
            if height[l] > height[r]:
                area = min(height[l], height[r]) * (r-l)
                r -= 1
            else: 
                area = min(height[l], height[r]) * (r-l)
                l += 1
            max_area = max(max_area, area)
        return max_area
            
                
        
        
        
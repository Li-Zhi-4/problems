class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Brute Force
        - Nested for loop
        - Record the max water per variation and record it
        - Return maximum water

        Optimized
        - Initialize l at 0
        - Initialize r at len(heights) - 1
        - Initialize max_water at 0
        - while l < r
            calculate curr_water, min(l,r value) * diff in l/r
            if curr_water > max_water, replace value
            if l < r value, l += 1
            else r -= 1
        - return max_water
        """
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            curr_water = min(heights[l], heights[r]) * (r-l)
            if curr_water > max_water:
                max_water = curr_water
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_water
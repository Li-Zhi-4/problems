class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        minTot = []

        l = 0
        for i in range(len(height)):
            maxLeft.append(l)
            if height[i] > l:
                l = height[i]

        r = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight.append(r)
            if height[i] > r:
                r = height[i]        
        maxRight.reverse()

        for i in range(len(height)):
            minTot.append(min(maxRight[i], maxLeft[i]))

        res = 0
        for idx, h in enumerate(height):
            tot = minTot[idx] - h
            if tot > 0:
                res += tot
        

        return res
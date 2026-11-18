class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute Force
        - Initialize counter to 0
        - For every element in the outer loop
            Loop through the nested loop starting at the outer element
            Record the max substring
        - Return the max substring
        Time: n^2
        Space: 1

        Optimized
        - Initialize counter to 0
        - Initialize l to 0
        - Initialize seen as set()

        - for r in range(len(s))
            while s[r] in seen
                seen remove s[l]
                l += 1
            seen add s[r]
            counter = max(counter, r - l + 1)        

        - return counter
        """
        counter = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            counter = max(counter, r - l + 1)

        return counter
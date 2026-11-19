class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        1. frequency counter of window
        2. if the frequency counter matches the p
        3. fixed
        """

        freq_p = {}
        for c in p:
            freq_p[c] = freq_p.get(c, 0) + 1
        
        l = 0
        indices = []
        freq_s = {}
        for r in range(len(s)):
            freq_s[s[r]] = freq_s.get(s[r], 0) + 1
            if r - l + 1 > len(p):
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    del freq_s[s[l]]
                l += 1
            if freq_s == freq_p:
                indices.append(l)
        return indices
            

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        for c in s1:
            hash1[c] = 1 + hash1.get(c, 0)

        hash2 = {}
        l = 0
        r = len(s1)
        while r < len(s2) + 1:
            for c in s2[l:r]:
                hash2[c] = 1 + hash2.get(c, 0)
            if hash1 == hash2:
                return True
            l += 1
            r += 1
            hash2 = {}
        
        return False
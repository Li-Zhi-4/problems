class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}

        for idx in range(len(s)):
            if s[idx] not in map1:
                map1[s[idx]] = 1
            else:
                map1[s[idx]] += 1
            
            if t[idx] not in map2:
                map2[t[idx]] = 1
            else:
                map2[t[idx]] += 1

        return map1 == map2


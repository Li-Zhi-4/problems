class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}

        for idx in range(len(s)):
            map1[s[idx]] = 1 + map1.get(s[idx], 0)
            map2[t[idx]] = 1 + map2.get(t[idx], 0)

        return map1 == map2


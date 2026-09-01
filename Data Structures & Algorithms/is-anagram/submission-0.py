class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}

        for idx in range(len(s)):
            if s[idx] not in letters:
                letters[s[idx]] = 1
            else:
                letters[s[idx]] += 1
            
            if t[idx] not in letters:
                letters[t[idx]] = -1
            else:
                letters[t[idx]] -= 1

        for nums in letters.values():
            if nums > 0:
                return False
        
        return True


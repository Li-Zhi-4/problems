class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for w in strs:
            w_sorted = "".join(sorted(w))
            if w_sorted in words:     # Check the dictionary, not the input list
                words[w_sorted].append(w)
            else:
                words[w_sorted] = [w]
        
        return list(words.values())

        
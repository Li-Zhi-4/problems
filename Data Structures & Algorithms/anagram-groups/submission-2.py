class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for s in strs:
            s_sorted = sorted(s)
            if "".join(s_sorted) in ana.keys():
                ana["".join(s_sorted)].append(s)
            else:
                ana["".join(s_sorted)] = [s]
        
        res = []
        for v in ana.values():
            res.append(v)

        return res
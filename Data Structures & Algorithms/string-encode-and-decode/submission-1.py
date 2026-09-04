class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        size = []
        res = []
        for s in strs:
            size.append(len(s))
        for sz in size:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        idx = s.find('#')
        l = s[0:idx-1].split(',')
        ans = []
        left, right = idx + 1, 0
        for w in l:
            right = left + int(w)
            ans.append(s[left:right])
            left = right
        return ans
        
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        b = { "(": ")", "[": "]", "{": "}" }
        for r in range(len(s)):
            if s[r] in b.keys():
                stack.append(s[r])
            elif not stack or s[r] != b[stack.pop()]:
                return False
        return not stack



        
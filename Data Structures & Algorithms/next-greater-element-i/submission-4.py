class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        ans = {}
        stack = []

        for r in range(len(nums2)):
            while stack and nums2[r] > stack[-1]:
                k = stack.pop()
                ans[k] = nums2[r]
            stack.append(nums2[r])

        for i in range(len(nums1)):
            res.append(ans.get(nums1[i], -1))

        return res
                     

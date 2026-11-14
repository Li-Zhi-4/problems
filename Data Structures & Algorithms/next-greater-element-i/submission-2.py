class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i, n1 in enumerate(nums1):
            run = 0
            for j, n2 in enumerate(nums2):
                if n1 == n2:
                    while j < len(nums2):
                        if nums2[j] > n1:
                            run = nums2[j]
                            break
                        j += 1

            print(run)
            if run == 0:
                res.append(-1)
            else:
                res.append(run)
    
        return res
                     

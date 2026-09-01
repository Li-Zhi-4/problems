class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # lookup table, save indexes when sorting nums
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = A[left][0] + A[right][0]
            
            if current_sum == target:
                return [
                    min(A[left][1], A[right][1]), 
                    max(A[left][1], A[right][1])
                ]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

        



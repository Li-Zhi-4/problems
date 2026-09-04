class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero = 0
        for n in nums:
            if n:
                total_prod *= n
            else:
                zero += 1

        if zero > 1:
            return [0] * len(nums)

        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            if zero:
                ans[i] = 0 if n else total_prod
            else:
                ans[i] = total_prod // n
        return ans

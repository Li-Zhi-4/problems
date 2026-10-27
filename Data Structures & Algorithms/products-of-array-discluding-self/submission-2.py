class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product = 1

        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                product *= n

        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                res = [0] * len(nums)
                res[i] = product
                break
            else:
                res[i] = product // nums[i]

        return res

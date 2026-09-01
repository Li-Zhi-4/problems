class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty_set = {x for x in nums}
        # return not (len(empty_set) == len(nums))
        empty_set = set()
        for x in nums:
            orig_l = len(empty_set)
            empty_set.add(x)
            if orig_l == len(empty_set):
                return True
        return False

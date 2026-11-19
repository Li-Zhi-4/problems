class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Tracking: duplicates within k distance
        Condition: r - l + 1 <= k
        Type: ?


        """
        seen = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            while r - l + 1 > k:
                seen.remove(nums[l])
                l += 1
        return False
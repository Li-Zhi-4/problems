class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        res = []
        for i in range(k):
            maxValue = max(count, key=count.get)
            res.append(maxValue)
            count.pop(maxValue)

        return res
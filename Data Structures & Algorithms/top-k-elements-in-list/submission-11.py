class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            # { 1: 1, 2: 2, 3: 3 }
            buckets[c].append(n)

        res = []
        for c in range(len(buckets) - 1, 0, -1):
            for n in buckets[c]:
                res.append(n)
                if len(res) == k:
                    return res
class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
            const seen = new Map()
    for (const [i, x] of nums.entries()) {
        if (seen.has(target - x)) return [seen.get(target-x), i];
        seen.set(x, i)
    }
    return []
    }
}

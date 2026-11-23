class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
            const seen = new Set()
    for (const x of nums) {
        if (seen.has(x)) return true;
        seen.add(x)
    }
    return false
    }
}

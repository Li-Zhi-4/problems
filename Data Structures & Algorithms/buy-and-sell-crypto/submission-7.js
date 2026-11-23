class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
            var minPrice = Infinity
    var best = 0
    for (const p of prices) {
        minPrice = Math.min(minPrice, p)
        best = Math.max(best, p - minPrice)
    }
    return best
    }
}

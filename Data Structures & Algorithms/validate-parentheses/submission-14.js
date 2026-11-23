class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
            const pairs = { ")": "(", "]": "[", "}": "{" }
    const stack = []
    for (const ch of s) {
        if (pairs[ch]) {
            if (stack.length === 0 || stack.at(-1) !== pairs[ch]) return false;
            stack.pop()
        } else {
            stack.push(ch)
        }
    }
    return stack.length === 0
    }
}

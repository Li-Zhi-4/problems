class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {   
         if (s.length !== t.length) return false;
    const count = {}
    for (const ch of s) count[ch] = (count[ch] ?? 0) + 1;
    for (const ch of t) {
        if ((count[ch] ?? 0) === 0) return false;
        count[ch] -= 1
    }
    return true
    }
}

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
            let l = 0
    let r = s.length - 1
    while (l < r) {
        if (!/[a-z0-9]/i.test(s[l])) l += 1;
        else if (!/[a-z0-9]/i.test(s[r])) r -= 1;
        else if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
        else {
            l += 1
            r -= 1
        }
    }
    return true
    }
}

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r  = 0, len(s) - 1
        def check(l, r, k):
            while l < r:
                if s[l] != s[r]:
                    if k == 0:
                        return False
                    return check(l + 1, r, k - 1) or check(l, r - 1, k - 1)
                l, r = l + 1, r - 1
            return True
        return check(l, r, 1)

        
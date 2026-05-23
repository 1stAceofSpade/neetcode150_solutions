from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        maxl = 0
        for char_code in range(ord('A'), ord('Z') + 1):
            target = chr(char_code)
            l = 0
            c = k
            for r in range(len(s)):
                if s[r] != target:
                    c -= 1
                while c < 0:
                    if s[l] != target:
                        c += 1
                    l += 1
                maxl = max(maxl, r - l + 1)
        return maxl
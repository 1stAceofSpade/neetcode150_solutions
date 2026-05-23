class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0 , 0
        size = len(s)
        length , max_length = 0 , 0
        seen = set()
        for r in range(size):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            length = r-l+1
            max_length = max(length , max_length)
        return max_length
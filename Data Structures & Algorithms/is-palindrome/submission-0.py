class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for ch in s.lower():
            if ch.isalnum():
                chars.append(ch)

        cleaned = "".join(chars)
        l , r =0 , len(cleaned) - 1
        while l<r:
            if cleaned[l] == cleaned[r]:
                l+=1
                r-=1
                continue
            return False
        return True
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lock , key = 1 , 1
        size1 , size2 = len(s1) , len(s2)
        l , r = 0 , 0
        for i in range(size1):
            lock *= (ord(s1[i]) - ord('a') + 2)
        for r in range(size2):
            size = r-l+1
            if size < size1:
                key*=(ord(s2[r]) - ord('a') + 2)
                continue
            if size == size1:
                key*= (ord(s2[r]) - ord('a') + 2)
                if lock == key:
                    return True
                else:
                    key = key//(int(ord(s2[l]) - ord('a') + 2))
                    l+=1
        return False
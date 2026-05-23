from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lock , key = 1 , 1
        size1 , size2 = len(s1) , len(s2)
        l , r = 0 , 0
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101
]
        for ch in s1:
            lock *= primes[ord(ch) - 97]
        for r in range(size2):
            size = r-l+1
            if size < size1:
                key*= primes[ord(s2[r]) - 97]
                continue
            if size == size1:
                key*= primes[ord(s2[r]) - 97]
                if lock == key:
                    return True
                else:
                    key = key//primes[ord(s2[l]) - 97]
                    l+=1
        return False
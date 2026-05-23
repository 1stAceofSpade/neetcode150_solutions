from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lock , key = 1 , 1
        size1 , size2 = len(s1) , len(s2)
        if size1 > size2:
            return False
        l , r = 0 , 0
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101
]
        MOD = 10**9 + 7
        mod_inverse = [pow(p , MOD-2 , MOD) for p in primes]
        for ch in s1:
            lock = (lock*(primes[ord(ch) - 97]))%MOD
        for r in range(size2):
            size = r-l+1
            if size < size1:
                key = (key*(primes[ord(s2[r]) - 97]))%MOD
                continue
            if size == size1:
                key = (key*(primes[ord(s2[r]) - 97]))%MOD
                if lock == key:
                    return True
                else:
                    key= (key*mod_inverse[ord(s2[l]) - 97])%MOD
                    l+=1
        return False
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find('#' , i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            ans.append(word)
            i=j+length+1
        return ans
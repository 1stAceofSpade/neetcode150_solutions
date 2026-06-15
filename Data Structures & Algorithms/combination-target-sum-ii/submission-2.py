class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        print(candidates)
        def backtrack(ind , path, target):
            if target==0:
                result.append(path[:])
                return
            if ind>=len(candidates):
                return
            if candidates[ind]<=target:
                path.append(candidates[ind])
                backtrack(ind+1 , path, target-candidates[ind])
                path.pop()
            nxt = ind+1
            while nxt < len(candidates) and candidates[nxt] == candidates[ind]:
                nxt += 1
            backtrack(nxt , path, target)

        backtrack(0 , [], target)
        return result
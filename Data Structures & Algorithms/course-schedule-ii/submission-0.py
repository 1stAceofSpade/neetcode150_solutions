class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i:[] for i in range(numCourses)}
        for cor,pre in prerequisites:
            preMap[cor].append(pre)
        visited = set()
        cycle = set()
        ans = []
        def dfs(cor):
            if cor in cycle:
                return False
            if cor in visited:
                return True
            cycle.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            cycle.remove(cor)
            visited.add(cor)
            ans.append(cor)
            return True
        for cor in range(numCourses):
            if dfs(cor)==False:
                return []
        return ans
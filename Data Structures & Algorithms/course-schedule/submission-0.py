class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for cor , pre in prerequisites:
            preMap[cor].append(pre)
        visited = set()
        def dfs(cor):
            if cor in visited:
                return False
            if preMap[cor]==[]:
                return True
            visited.add(cor)
            for pre in preMap[cor]:
                if not dfs(pre): return False
            visited.remove(cor)
            preMap[cor]=[]
            return True
        for cor in range(numCourses):
            if not dfs(cor): return False
        return True
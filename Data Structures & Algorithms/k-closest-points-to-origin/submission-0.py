import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x , y in points:
            d = x**2 + y**2
            heapq.heappush(heap , [-d , [x , y]])
            size = len(heap)
            if size>k:
                heapq.heappop(heap)
        return [point for _,point in heap]
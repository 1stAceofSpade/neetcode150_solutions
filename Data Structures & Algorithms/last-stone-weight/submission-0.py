import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heapq.heappush(heap , -n)
        while len(heap)>1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y!=x:
                heapq.heappush(heap , -(y-x))
        if len(heap)>0:
            return -heap[0]
        else:
            return 0
        
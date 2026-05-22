import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x1 = -heapq.heappop(heap)
            x2 = -heapq.heappop(heap)
            weight = x1-x2
            heapq.heappush(heap, -weight)
        return -heap[0]
            
                    


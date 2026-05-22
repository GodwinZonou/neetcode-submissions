import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        heapq.heapify(self.heap)
        self.position = k

    def add(self, val: int) -> int:
        heap = self.heap
        heapq.heappush(heap, val)
        position = self.position
        while len(heap)>position:
            heapq.heappop(heap)
        return self.heap[0]
        

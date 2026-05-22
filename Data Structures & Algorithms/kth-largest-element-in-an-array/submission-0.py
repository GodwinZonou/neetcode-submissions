import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums, reverse=True)[k-1]
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]
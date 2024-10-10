import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Initialize empty min heap
        min_heap = []
        for num in nums:
            # Add numbers until minimum size is reached
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                # If the root is less than num in list replace root with num
                if num > min_heap[0]:
                    heapreplace(min_heap, num)

        # Return the root node which is the kth biggest element
        return min_heap[0]

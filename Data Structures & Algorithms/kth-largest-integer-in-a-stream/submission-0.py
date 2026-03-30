class KthLargest:

    #kör minheap med dem k största elementen, där rooten är den minsta, dvs den kth största

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        print(f"starting heap {self.heap}")

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

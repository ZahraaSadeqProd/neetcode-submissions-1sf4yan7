class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for coords in points:
            x, y = coords

            val = math.sqrt((x)**2 + (y)**2)
            heap.append([val, x, y])


        heapq.heapify(heap)

        for i in range(k):
            val, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
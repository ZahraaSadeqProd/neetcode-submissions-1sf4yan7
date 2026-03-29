class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        coresCoords = {}
        res = []

        for coords in points:
            x, y = coords

            val = math.sqrt((x)**2 + (y)**2)
            heap.append(val)

            if val not in coresCoords:
                coresCoords[val] = [[x, y]]
            else:
                coresCoords[val].append([x, y])


        heapq.heapify(heap)

        for i in range(k):
            val = heapq.heappop(heap)
            arr = coresCoords[val]
            res.append(arr[0])
            arr = arr[1:]
            coresCoords[val] = arr
        return res
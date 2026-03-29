class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        stones[i] == i

        sim


        chose heaviest stone x and y

        if x == y:
            pop(x)
            pop(y)

        if x < y:
            pop(x)
            y = y - x


        """

        stones = [-x for x in stones]

        heapq.heapify(stones)


        while True:
            if len(stones) == 0:
                return 0

            if len(stones) == 1:
                return abs(stones[0])

            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            if abs(x) < abs(y):
                val = (abs(y) - abs(x)) * -1
                heapq.heappush(stones, val)
            else:
                val = (abs(x) - abs(y)) * -1
                heapq.heappush(stones, val)



        return 0

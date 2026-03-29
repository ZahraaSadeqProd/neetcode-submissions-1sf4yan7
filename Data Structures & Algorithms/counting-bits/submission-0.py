class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1) 

        for i in range(n + 1):
            count = 0
            j = i
            while j:
                if j % 2:
                    count += 1
                j = j >> 1
            arr[i] = count

        return arr
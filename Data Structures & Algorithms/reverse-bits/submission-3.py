class Solution:
    def reverseBits(self, n: int) -> int:
        j = 0
        val = 0

        for i in range(32):
            val = val << 1
            if (1 << i) & n:
                val += 1


        print("{0:b}".format(val))


        return val
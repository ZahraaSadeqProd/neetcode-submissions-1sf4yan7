class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()

            if x == y:
                continue
            if x < y:
                # calculate new value
                val = y - x

                # BS to find where to insert it
                L, R = 0, len(stones) - 1
                mid = (L + R) // 2
                
                while L <= R:
                    mid = (L + R) // 2

                    if val > stones[mid]:
                        L = mid + 1
                    elif val < stones[mid]:
                        R = mid - 1
                    else:
                        break
                    
                # else we found where we can insert it 
                stones.append(0)

                # stones.insert(L, val)
                # 1 2 3 4 5 0
                #     ^



                # for n in range(L, len(stones) - 1):
                #     tmp = stones[n + 1]
                #     stones[n + 1] = stones[n]

                for n in range(len(stones) - 1, L, -1):
                    stones[n] = stones[n - 1]

                stones[L] = val

        stones.append(0)
        return stones[0]












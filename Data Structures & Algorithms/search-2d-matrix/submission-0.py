class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        mid = (R + L) // 2
        idx = -1
        
        while L <= R:
            mid = (R + L) // 2

            if target > matrix[mid][0] and target > matrix[mid][-1]:
                L = mid + 1 
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                idx = mid
                break

        if idx != -1:
            L, R = 0, len(matrix[idx]) - 1
            mid = (R + L) // 2

            while L <= R:
                mid = (R + L) // 2
                
                if target > matrix[idx][mid]:
                    L = mid + 1
                elif target < matrix[idx][mid]:
                    R = mid - 1
                else:
                    return True

        return False

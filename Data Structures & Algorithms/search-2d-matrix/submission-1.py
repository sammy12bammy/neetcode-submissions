class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find out what row it's in
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            row = top + ((bot - top) // 2)
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                # target is in this row, search within it
                break
        else:
            return False  # no valid row found
        
        # binary search within the row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            col = l + ((r - l) // 2)
            if matrix[row][col] > target:
                r = col - 1
            elif matrix[row][col] < target:
                l = col + 1
            else:
                return True
        return False
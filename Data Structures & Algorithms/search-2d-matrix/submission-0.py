class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        
        while(l<=r):
            mid = (l + r)//2
            curr = mid
            row = curr//len(matrix[0])
            col = curr%len(matrix[0])
            
            if matrix[row][col] == target:
                return True
            elif(matrix[row][col] < target):
                l = mid + 1
            else:
                r = mid - 1
        return False
            
            
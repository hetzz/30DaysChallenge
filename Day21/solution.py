# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        rows = dimensions[0] - 1
        cols = dimensions[1] - 1
        
        result = -1
        
        if rows == 0 or cols == 0:
            return -1
        
        while(rows >= 0 and cols >= 0):
            print(binaryMatrix.get(rows,cols),rows,cols)
            if binaryMatrix.get(rows,cols):
                result = cols
                cols -= 1 
            else:
                rows-=1
        
        
        return result
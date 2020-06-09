class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n == 0:
            return False
        if n < 0:
            return False
        if int(math.log(n,2)) == math.log(n,2):
            return True
        return False
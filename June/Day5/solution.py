class Solution:
    def __init__(self, w):
        for i in range(1,len(w)):
            w[i] = w[i-1] + w[i]
        self.w = w

    def pickIndex(self) -> int:
        import random
        rand = random.randint(1, self.w[-1])
        l = 0
        r = len(self.w) -1
        while l <= r:
            mid = (l+r)//2
            if rand >= self.w[mid] and rand <= self.w[mid+1]:
                return mid +1
            elif rand <= self.w[mid] and rand >= self.w[mid-1]:
                return mid 
            else:
                if rand > self.w[mid]:
                    l = mid +1
                else:
                    r = mid - 1

o = Solution([[[1,3]],[],[],[],[],[]])

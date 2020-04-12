def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        if abs(stones[-1] - stones[-2]) != 0 :
            stones [-2] = abs(stones[-1] - stones[-2])
            stones = stones[:-1]
        else:
            stones = stones[:-2]
    return stones[0] if stones else 0

stones = [2,2]
print(lastStoneWeight(stones))
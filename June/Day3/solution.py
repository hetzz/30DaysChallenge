class Solution:
    def twoCitySchedCost(self, costs):
        sum_of_first = [i for i,j in costs]
        negative_of_first = [j - i for i,j in costs]
        return sum(sum_of_first) + sum(sorted(negative_of_first)[:len(costs)//2])
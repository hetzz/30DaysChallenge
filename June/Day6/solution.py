class Solution:
    def reconstructQueue(self, people):
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result
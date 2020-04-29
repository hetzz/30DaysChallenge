class FirstUnique:

    def __init__(self, nums):
        self.queue = []
        self.dict = {}
        for i in nums:
            if self.dict.get(i):
                self.dict[i] += 1
            else:
                self.dict[i] = 1
        for key,value in self.dict.items():
            if value == 1:
                self.queue.append(key)

    def showFirstUnique(self):
        return self.queue[0] if self.queue else -1

    def add(self, value):
        if not self.queue.count(value) and not self.dict.get(value):
            self.queue.append(value)
        else:
            try:
                self.queue.remove(value)
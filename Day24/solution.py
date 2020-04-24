import math
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.order.remove(key)
        elif len(self.cache) >= self.capacity :
            self.cache.pop(self.order[0])
            self.order = self.order[1:]
        self.cache[key] = value
        self.order.append(key)

cache = LRUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

'''
Another approach
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict
            
		self.cache[key] = value
'''
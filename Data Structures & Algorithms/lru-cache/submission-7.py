class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.usage = []

    def get(self, key: int) -> int:
        if key in self.usage:
            self.usage.remove(key)
            self.usage.insert(0, key)

        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.usage:
            self.usage.remove(key)
        self.usage.insert(0, key)
        
        leastRecentlyUsedKey = ""

        if len(self.usage) > self.capacity:
            leastRecentlyUsedKey = self.usage.pop()

        if leastRecentlyUsedKey in self.cache:
            del self.cache[leastRecentlyUsedKey]
            # self.cache.pop(leastRecentlyUsedKey, None)

        self.cache[key] = value
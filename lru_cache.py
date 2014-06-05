class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache_used = 0
        self.capacity = capacity
        self.head = ["H", None, None, "H"]
        self.tail = ["T", None, None, "T"]
        self.head[2] = self.tail
        self.tail[1] = self.head
        self.cache_map = {}

    # @return an integer
    def get(self, key):
        if key in self.cache_map:
            self.cache_map[key][2][1] = self.cache_map[key][1]
            self.cache_map[key][1][2] = self.cache_map[key][2]
            self.cache_map[key][1] = self.head
            self.cache_map[key][2] = self.head[2]
            self.head[2][1] = self.cache_map[key]
            self.head[2] = self.cache_map[key]
            return self.cache_map[key][0]
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache_map:
            self.cache_map[key][2][1] = self.cache_map[key][1]
            self.cache_map[key][1][2] = self.cache_map[key][2]
            self.cache_map[key][1] = self.head
            self.cache_map[key][2] = self.head[2]
            self.head[2][1] = self.cache_map[key]
            self.head[2] = self.cache_map[key]
            self.cache_map[key][0] = value
        else:    
            if self.cache_used == self.capacity:
                self.cache_map.pop(self.tail[1][3], None)
                self.tail[1] = self.tail[1][1]
                self.tail[1][2] = self.tail
                self.cache_used -= 1
            self.cache_used += 1
            self.cache_map[key] = [value, self.head, self.head[2], key]
            self.head[2][1] = self.cache_map[key]
            self.head[2] = self.cache_map[key]

    def print_list(self):
        head = self.head
        while head != None:
            print head[3],
            head = head[2]
        print

    def print_reverse(self):
        tail = self.tail
        while tail != None:
            print tail[3],
            tail = tail[1]
        print

cache = LRUCache(3)

cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
cache.set(4,4),
print cache.get(4)
print cache.get(3)
print cache.get(2)
print cache.get(1)
cache.set(5,5)
print cache.get(1)
print cache.get(2)
print cache.get(3)
print cache.get(4)
print cache.get(5)

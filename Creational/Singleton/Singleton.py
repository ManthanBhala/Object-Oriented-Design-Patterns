class Cache:

    def __init__(self, size):
        self.size = size
        self.cache = [-1] * size
    
    def get(self, key):
        return self.cache[key]
    
    def put(self, key, value):
        self.cache[key] = value
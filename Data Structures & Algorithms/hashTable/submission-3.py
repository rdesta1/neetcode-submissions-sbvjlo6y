class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.map = [None for i in range(self.capacity)]

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if not self.map[index]:
                self.map[index] = Pair(key, value)
                self.length += 1
                if self.length >= self.capacity // 2:
                    self.resize()
                break
            elif self.map[index].key == key:
                self.map[index].val = value
                break
            index += 1
            index %= self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index]:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index %= self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        if self.map[index] == None:
            return False
        
        while self.map[index].key:
            if self.map[index].key == key:
                self.map[index] = None
                self.length -= 1
                return True
            index += 1
            index %= self.capacity 
        return False

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        newmap = [None for i in range(self.capacity)]
        oldmap = self.map
        self.map = newmap
        self.length = 0
        for pair in oldmap:
            if pair:
                self.insert(pair.key, pair.val)

    def hash(self, key):
        return key % self.capacity
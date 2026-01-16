class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None]* self.size
        self.data = [None]* self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value
                    

    
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def hash_function(self, key):
        return key % self.size
        
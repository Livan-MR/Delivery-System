class Hashmap:

    # Constructor for initial parameters
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size


    # function that returns hash
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size


    # Functon to insert values into hashmap.
    # First checks to see if key is taken and adds to hashmap.
    # If key is taken then we will replace old key with new key.
    def insert(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                        pair[1] = value
                        return True
            self.map[key_hash].append(key_value)
            return True


    # Search for pair when given a key
    def search(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


    # Searches for given key and then deletes key if found
    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] == None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

hashtable = Hashmap()
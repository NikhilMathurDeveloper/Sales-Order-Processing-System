
class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class hashTable:
    def __init__(self):
        self.capacity = 20
        self.numBuckets = [None] * self.capacity
    def hash(self, key):
        sum = 0
        for i in range(0,len(key)):
            ascii_code = ord(key[i])
            sum = sum +ascii_code
        hash_value  = sum % self.capacity

        return hash_value
    def insert(self, key, value):
        index = self.hash(key)
        pair = [key, value]

        if self.numBuckets[index-1] == None:
            self.numBuckets[index-1] = pair

            print(self.numBuckets)
        else: 
            while self.numBuckets[index-1] is not None:
                index+=1
            self.numBuckets[index-1] = pair
            print(self.numBuckets)
       


    def search(self, key):
        index = self.hash(key)
        
        if self.numBuckets[index-1] != None:
            print(self.numBuckets[index-1])
        else:
            if self.numBuckets[index-1] == None:
                index +=1
            
c = hashTable()


c.insert("Mate", 3)
c.insert("Velo", 4)

c.search("Hello")





        
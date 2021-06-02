#HashTable, very good for lookups and is a ds that maps keys to value.
'''
Hashtable is very good for when we want to do quick lookups,insertion or deletion, otherwise is not a convenient ds to use
Big(0)
Access
insert:O(1)
deletion:O(1)
search:O(1)

'''
CAPACITY = 50

class Node:
    def __init(self,key,value):
        self.key = key
        self.value = value
        self.next= None

class HashTable:
    def __init(self):
        self.capacity = CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self,key):
        hashSum = 0
        for index, i in enumerate(key):
            hashSum+= (index + len(key) ** ord(i))
            hashSum = hashSum % self.capacity

    def insert(self,key,value):
        self.size +=1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key,value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key,value)

    def find(self,key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return  node.value

    def remove(self,key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -=1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result




        

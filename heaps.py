'''
Heap min :The elements are all smaller than their children
Heap max: The elements are all bigger than their children
Trie: trees that allows us to store words
'''
import sys
class MinHeap:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.Heap = [0] * (self.maxSize +1)
        self.Heap[0] = -1 * sys.maxsize
        self.Front = 1
    def parent(self,position):
        return position //2
    def swap(self,fpos,spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    def insert(self,ele):
        if self.size >= self.maxSize:
            return
        self.size +=1
        self.Heap[self.size] = ele
        curr = self.size
        while self.Heap[curr] < self.Heap[self.parent(curr)]:
            self.swap(curr,self.parent(curr))
            curr = self.parent(curr)

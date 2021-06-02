
'''
Big O
Delete IS 0(n)
insert is 0(1)
search is o(n)
Arraylist is not really useful if we are searching for an element since we have to loop the array, but the advantage is that we can re-size the array and insertion is very quick

'''


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = self.array(self.capacity)

    def array(self,len):
        return [None] * len

    def resize(self,new_capacity):
        new_array = self.array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array
        self.capacity = new_capacity

    def add(self,ele):
        if self.size == self.capacity:
            self.resize(2*self.capacity)

        self.arr[self.size] = ele
        self.size += 1

    def remove(self):

        element = None

        if self.size > 0:
            element = self.arr[self.size -1]
            self.arr[self.size -1] = None
            self.size -=1
            if self.size <= self.capacity //4:
                self.resize(self.capacity//2)

        return  element
    def search(self,value):
        for i in range(0,self.size):
            print(i)
            if value == self.arr[i]:
                print('value found')
                return self.arr[i]
        print('value not found')
        return None




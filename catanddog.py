from queue import  Queue
class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.arrival = []

    def dequeueCat(self):
        if self.cat.isEmpty():
            return 'No cat present'
        cat = self.cat
        v = cat.remove()
        return v
    def dequeueDog(self):
        if self.dog.isEmpty():
            return 'No dogs are present'
        dog = self.dog
        v = dog.remove()
        return v

    def adopt_specific(self,type):
        if type == 'Dog':
            self.dequeueDog()
        if type == 'cat':
            self.dequeueCat()
    def enqueue(self,name,type):
        if type == 'dog':
            self.dog.add(name)
            self.arrival.append(type)
        if type == 'cat':
            self.cat.add(name)
            self.arrival.append(type)

    def dequeuAny(self):

        v = self.arrival.pop(0)
        if v == 'dog':
            self.dequeueDog()
        if v == 'cat':
            self.dequeueCat()


if __name__ == "__main__":
    a = AnimalShelter()
    a.enqueue('c','cat')
    a.dequeueCat()







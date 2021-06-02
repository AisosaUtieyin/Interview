#Linkedlist is a basic ds that stores item sequentialy, each item has a pointer that referec to the location of the other iten.
'''
Eachh item is called a node, the first Node is called the head, the last Node is called tail
CONS
finding an element is slow
PROS
inserting at the tail and deleting at the head are extremely fast operations
you don't need to specify the size unlike an array. So you can add elements as long as you do not surpass the space of the machine
BIG(O)
Access : O(n)
Insert: 0(1)
Deletion : 0(n)
Search: 0(n)
'''
#Doubly LinkedList is just like a linked list but the pointers refere to th next node and the previous node so traversing backward is easy
'''
Pros and cons same as linkedlist same as big o
'''

class Node:
    def __init__(self,item = None):
        self.item = item
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node
    def pre_append(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self,value):
        current = self.head
        if current is None:
            return
        while (current.next is not None):
            if(current.next.data == value):
                current.next = current.next.next
                return
        if current.data == value:
            current = current.n




a = Linked_List()
a.append(4)
print(a)




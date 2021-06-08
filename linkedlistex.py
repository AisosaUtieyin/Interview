class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def pre_append(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        if current is None:
            return
        while (current.next is not None):
            if (current.next.data == value):
                current.next = current.next.next
                return
        if current.data == value:
            current = current.n

    def print_list(self):
        node = self.head
        listOfNodes = []
        while node:
            listOfNodes.append(node.item)
            node = node.next
        print(listOfNodes)

    def remove_dups(self):
        prev = self.head
        node = prev.next

        values = []
        while node is not None:
            if node.item in values:
                prev.next = prev.next.next

            values.append(node.item)
            node = node.next
            prev = prev.next

    def return_kthToLast(self, n):
        node = self.head
        counter = 0
        second_counter = 0
        while node is not None:
            counter += 1
            node = node.next
        result = counter - n
        node = self.head
        while node is not None:
            second_counter += 1
            if second_counter == result:
                val = node.item
                return val
            else:

                node = node.next

    def delete_middleNode(self):
        node = self.head
        c = 0
        v = 0

        while node is not None:
            c += 1
            v = 0
            node = node.next
        c = c // 2
        prev = self.head
        node = prev.next
        while prev is not None:
            v += 1
            if v == c - 1:
                prev.next = prev.next.next
            else:
                node = node.next
                prev = prev.next

    def partition(self,n):
        node = self.head
        head = node
        tail = node
        while node is not None:
            next_node = node.next
            if node.item < n:
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = next_node
        tail.next = None
        self.head = head

    def sum_lists(self,list):
        p = self.head
        q = list.head
        sumList = Linked_List()
        c = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.item
            if not q:
                j = 0
            else:
                j = q.item
            s = i+j+c
            if s>=10:
                c = 1
                r = s %10
                sumList.append(r)
            else:
                c =0
                sumList.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sumList.print_list()

    def palindrome(self):
        node = self.head
        c = 0
        i = 0
        values = []
        reversed_values = []
        while node:
            c +=1
            values.append(node.item)
            reversed_values.append(node.item)
            node = node.next
        values.reverse()
        if reversed_values == values:
            return True
        else:
            return False
    def intersection(self,a):
        visited = set()
        curA = self.head
        curB = a.head
        while curA:
            visited.add(curA)
            curA = curA.next
        while curB:
            if curB in visited:
                return curB
            curB = curB.next
        return None
    def loop_detection(self):
        pass
















if __name__ == "__main__":
   a = Linked_List()
   a.append(1)
   a.append(2)
   a.append(0)
   a.append(2)
   a.append(1)
   print(a.palindrome())
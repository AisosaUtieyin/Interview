'''
A type of binary tree which fullfils a specif ordering property(subtree of leftnodes are less than the root nodes which is
less than all the right nodes.
Traversing a binary search tree can be done in 3 ways.
1)PreOrder (Root-Left-Right)
2)InOrder(Left-Root-Right)
3)PostOrder(Left-right-root)
Big O notation
Access: Θ(log(n))
Search:Θ(log(n))
Insert:Θ(log(n))
Delete:Θ(log(n))
Advantage
Much quicker than a serial search because the data that needs to be searched halves with each step.
'''
import random


class BST():
    def __init__(self, item=None):
        self.left = None
        self.right = None
        self.item = item
        self.values = []

    def insert(self, value):
        if not self.item:
            self.item = value
            self.values.append(value)
            return
        if self.item == value:
            return
        if value <= self.item:
            if self.left:
                self.left.insert(value)
                self.values.append(value)
                return
            self.left = BST(value)
            self.values.append(value)
            return
        if value > self.item:
            if self.right:
                self.right.insert(value)
                self.values.append(value)
                return
            self.right = BST(value)
            self.values.append(value)
            return

    def find(self, value):
        if self.item == value:
            return True
        if value < self.item:
            if self.left == None:
                return False
            self.left.find(value)
        if value > self.item:
            if self.right == None:
                return False
            self.right.find(value)

    def getRandomNode(self):
        r = random.randint(0, len(self.values))
        print(self.values[r])


    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        print(self.item)
        if self.right is not None:
            self.right.inOrder()

    def preOrder(self):
        if self.item is not None:
            print(self.item)
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()

    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.item)


def getOrder(t1, st):
    if (t1 == None):
        st += 'x'
        return
    st += str(t1.item) + " "
    getOrder(t1.left, st)
    getOrder(t1.right, st)


def containstree(t1, t2):
    s1 = ''
    s2 = ''
    getOrder(t1, s1)
    getOrder(t2, s2)

    return s1.index(str(s2)) != 1


def weave_list(f, s, r, p):
    if not f or s:
        r.append(p + f + s)
        return
    first_head, first_tail = f[0], f[1:]
    weave_list(first_tail, s, r, p + [first_head])

    second_head, second_tail = s[0], s[1:]
    weave_list(f, second_tail, r, p + [second_head])


def sequence(root):
    if root is None:
        return []
    ans = []
    prefix = [root.item]
    l = sequence(root.left) or [[]]
    r = sequence(root.right) or [[]]
    for i in range(len(l)):
        for j in range(len(r)):
            w = []
            weave_list(l[i], r[j], w, prefix)
        ans.extend(w)
    return ans


if __name__ == "__main__":
    a = BST(2)
    a.insert(1)
    a.insert(3)
    a.successor(1)
    
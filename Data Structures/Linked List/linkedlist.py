class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linked_list:
    def __init__(self):
        self.head=None

    def traverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current=current.ref

    def addend(self,data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            current = self.head
            while current.ref is not None:
                current = current.ref
            newnode = Node(data)
            current.ref = newnode

    def addbegin(self,data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            newnode.ref = self.head
            self.head = newnode

    def addafterx(self,x,data):
        if self.head is None:
            print("linked list is empty")

        else:
            current = self.head
            while current is not None:
                if current.data == x :
                    break
                current = current.ref

            if current is None:
                print("node not found")
            else:
                newnode = Node(data)
                newnode.ref = current.ref
                current.ref = newnode

    def addbefore(self,x,data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            current = self.head
            while current is not None:
                if current.ref.data == x:
                    break
                current=current.ref
            if current is None:
                print("node not found")
            else:
                newnode = Node(data)
                newnode.ref = current.ref
                current.ref = newnode

    def delfirst(self):
        if self.head is None:
            print("linked list is empty")
        else:
            self.head=self.head.ref

    def dellast(self):
        if self.head is None:
            print("linked list is empty")
        else:
            current = self.head
            while current.ref.ref is not None:
                current=current.ref
            current.ref = None

    def delbyx(self,x):
        if self.head is None:
            print("linked list is empty")

        else:
            current = self.head
            while current.ref is not None:
                if current.ref.data == x:
                    break
                current = current.ref
            if current is None:
                print("node not found")
            else:
                current.ref = current.ref.ref


    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            nextnode = current.ref
            current.ref = prev
            prev = current
            current = nextnode
        self.head = prev

######################################################################  
# this is how reverse works for linkedlist
#         Iteration 1:
# prev: None
# current: 1 -> 2 -> 3 -> 4 -> None

# first we will set nextnode as 2
# then we want to move None to right and we want to store the current , i,e 1 in the prev 
# so we will store None ,which is the prev to currents ref which means 1's ref
#  then we will move one upwards in the line prev = current and the None which is in the 1's ref will also follow
# and it will look like this => # prev: 1 -> None
# and thenthe nextnode which was 2 will move as the current and it will lool like this, this steps continue
                                # current: 2 -> 3 -> 4 -> Non                                
# prev: 2 -> 1 -> None
# current: 3 -> 4 -> None
# prev: 3 -> 2 -> 1 -> None
# current: 4 -> None
# prev: 4 -> 3 -> 2 -> 1 -> None
# current: None
########################################################################

    def arr(self, head):
        self.head = head
        current = self.head
        y = []
        while current is not None:
            y.append(current.data)
            current = current.ref
        y.sort()
        y.reverse()
        print(y)

    def tolinkedlist(self, arr):
        self.head = Node(arr[0])
        current = self.head
        for i in range(1, len(arr)):
            newnode = Node(arr[i])
            current.ref = newnode
            current = newnode


x=Linked_list()
x.addend(1)
x.addend(2)
x.addend(3)
x.addend(4)
x.addend(5)
x.arr(x.head)


x.traverse()





class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None

class Stack():
    def __init__(self):
        self.head = None
    def add(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head = newnode
        else:
            current = self.head
            while current.ref is not None:
                current=current.ref
            newnode=Node(data)
            current.ref = newnode


    def pop(self):
        if self.head is None:
            print("Stack is empty")
        current = self.head
        while current.ref.ref is not None:
            current = current.ref
        current.ref = None

    def traverse(self):
        if self.head is None:
            print("stack is empty")
        current = self.head
        while current is not None:
            print(current.data,end=" ")
            current = current.ref

    def deletemiddleelement(self):
        firstpointer = self.head
        prevofsecond = None
        secondpointer = self.head
        while firstpointer.ref is not None and firstpointer.ref.ref is not None:
            firstpointer = firstpointer.ref.ref
            prevofsecond = secondpointer
            secondpointer = secondpointer.ref
        prevofsecond.ref = secondpointer.ref
    
            
        
x=Stack()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(5)
x.deletemiddleelement()
x.traverse()
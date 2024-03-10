class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def Enqueue(self,data):
        if self.front is None:
            newnode=Node(data)
            self.front=newnode
            self.rear=newnode
        else:
            newnode=Node(data)
            self.rear.ref=newnode
            self.rear=newnode
    def Dequeue(self):
        if self.front is None:
            print("queue is empty")
        elif self.front.ref is  None:
            self.front=None
        else:
            temp=self.front
            self.front=temp.ref
            temp=None
    def Display(self):
        if self.front is None:
            print("queue is empty")
        else:
            current=self.front
            while current is not None:
                print(current.data)
                current=current.ref
x=Queue()
x.Enqueue(5)
x.Enqueue(10)
x.Enqueue(15)
x.Enqueue(20)
x.Enqueue(25)
x.Dequeue()
x.Display()



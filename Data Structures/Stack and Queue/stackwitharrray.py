class Stack:
    def __init__(self):
        self.arr = []

    def Push(self, data):
        self.arr.append(data)

    def Pop(self):
        if len(self.arr) == 0:
            print("Stack is empty")
        else:
            self.arr.pop()

    def Display(self):
        if len(self.arr) == 0:
            print("Stack is empty")
        else:
            reversed_array = self.arr[::-1]
            print(reversed_array)
    def delmid(self):
        mid = len(self.arr)//2
        self.arr.pop(mid)
x=Stack()
x.Push(5)
x.Push(10)
x.Push(15)
x.delmid()
x.Display()
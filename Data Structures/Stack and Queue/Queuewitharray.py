class Queue:
    def __init__(self):
        self.arr = []

    def Enqueue(self, data):
        self.arr.append(data)

    def Dequeue(self):
        if len(self.arr) == 0:
            print("Stack is empty")
        else:
            self.arr=self.arr[1:]

    def Display(self):
        if len(self.arr) == 0:
            print("Stack is empty")
        else:

                print(self.arr)
x=Queue()
x.Enqueue(10)
x.Enqueue(20)
x.Enqueue(30)
x.Enqueue(40)
x.Enqueue(50)
x.Dequeue()
x.Dequeue()
x.Display()

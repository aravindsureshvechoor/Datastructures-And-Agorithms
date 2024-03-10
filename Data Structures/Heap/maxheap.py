class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        n = len(self.heap)
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        max_value = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self.heapify_down(0)

        return max_value


max_heap = MaxHeap()


max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(1)
max_heap.insert(10)


max_element = max_heap.extract_max()
print("Maximum element:", max_element)


max_heap.insert(15)


max_element = max_heap.extract_max()
print("Updated maximum element:", max_element)

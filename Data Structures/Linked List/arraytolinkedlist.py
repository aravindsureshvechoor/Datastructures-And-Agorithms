class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def arraytoll(arr):
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        current.ref = new_node
        current = new_node

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data)
        current = current.ref

# Example usage
arr = [1, 2, 3, 4, 5]
head = arraytoll(arr)
print_linked_list(head)

# Implementation of binary search algorithm
def binary_search(arr, end_point):
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == end_point:
            return mid
        elif arr[mid] < end_point:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Implementing Queue using a single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating the class Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    # Creating the enqueue method
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # Creating the dequeue method
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


queue = Queue()

data_list = [1, 2, 5, 4, 9, 14, 18, 10, 20, 3, 7, 23, 25, 16, 12]

for dat in data_list:
    queue.enqueue(dat)

queue.display()

for _ in range(4):
    queue.dequeue()

queue.display()

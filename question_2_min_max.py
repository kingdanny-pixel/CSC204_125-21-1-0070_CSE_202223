# Creating the class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Method to display the maximum and minimum data in the single linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    # insert method
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    #display method
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    # method for getting the maximum value
    def get_max(self):
        if self.head is None:
            return None

        max_data = self.head.data
        current_node = self.head.next
        while current_node is not None:
            if current_node.data > max_data:
                max_data = current_node.data
            current_node = current_node.next

        return max_data

    # method for getting the minimum value
    def get_min(self):
        if self.head is None:
            return None

        min_data = self.head.data
        current_node = self.head.next
        while current_node is not None:
            if current_node.data < min_data:
                min_data = current_node.data
            current_node = current_node.next

        return min_data


linked_list = LinkedList()

data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
for data in data_list:
    linked_list.insert(data)


print("Maximum data:", linked_list.get_max())
print("Minimum data:", linked_list.get_min())

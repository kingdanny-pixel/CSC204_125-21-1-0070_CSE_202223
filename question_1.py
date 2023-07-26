# QUESTION 1

# Creating a node which has data and next as it should be in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# Creating a class for the Single Linked List
class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Creating the insert method
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            present_node = self.head
            while present_node.next_node:
                present_node = present_node.next_node
            present_node.next_node = new_node

    # Creating the display method
    def display(self):
        present_node = self.head
        while present_node:
            print(present_node.data, end=" --> ")
            present_node = present_node.next_node
        print("Null")


if __name__ == "__main__":
    linked_list = SingleLinkedList()

    dataset_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    for each_data in dataset_list:
        linked_list.insert(each_data)

    linked_list.display()

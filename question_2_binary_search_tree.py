from question_2_min_max import Node
# Method that converts the single linked list into a binary search tree.
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        present_node = self.head
        while present_node is not None:
            print(present_node.data)
            present_node = present_node.next

    # method for converting to a binary search tree
    def to_bst(self, dataset):
        if not dataset:
            return None

        mid = len(dataset) // 2
        root = Node(dataset[mid])
        root.left = self.to_bst(dataset[:mid])
        root.right = self.to_bst(dataset[mid+1:])

        return root


linked_list = LinkedList()

dataset = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
for data in dataset:
    linked_list.insert(data)

linked_list.to_bst(dataset)

linked_list.display()

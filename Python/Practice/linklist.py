class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="  -->  ")
            current = current.next

list1 = LL()
n = int(input("Enter the numbers of Elements? "))
for i in range(n):
    data = int(input("Enter data Item: "))
    list1.append(data)
print("The linked list: ", end="")
list1.display()

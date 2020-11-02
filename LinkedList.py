class Node:
    def __init__(self, val):
        self.data = val
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return "Linkedlist is Empty"

    def display(self):
        p = self.head
        while p.link:
            print("{}--->".format(p.data),end= "")
            p = p.link
        print(p.data)

    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.link
            current_node.link = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def insertAtBegin(self,val):
        b = Node(val)
        b.link = self.head
        self.head = b

    def insertAtEnd(self, val):
        a = Node(val)
        if self.head is None:
            self.head = a
            return
        p = self.head
        while p.link is not None:
            p = p.link
        p.link = a

    def search(self,val):
        p, i = self.head, 0
        while p:
            if p.data == val:return "Found at index {}".format(i)
            else:
                p = p.link
                i += 1
        else:return "Not Found"

    def insertAtPosition(self,val,pos):
        c = Node(val)
        p = self.head
        i = 1
        while i!= pos:
            p = p.link
            i += 1
        c.link = p.link
        p.link = c

    def remove_Last(self):
        p = self.head
        while(p.link is not None):
            prev  = p
            p = p.link
        prev.link = None

    def createLinkedList(self):
        size = int(input("Enter the number of Nodes: "))
        for i in range(size):
            data = input("Enter the data: ")
            self.insertAtEnd(data)

list = LinkedList()
list.createLinkedList()

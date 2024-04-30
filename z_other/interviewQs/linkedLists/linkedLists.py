'''
This file declares some classes for the construction of linked lists!!!
'''

# node for building a singley linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList():
    def __init__(self):
        self.head = None

    # time complextity O(1)
    def add_node_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # time complexity O(n)
    def add_node_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
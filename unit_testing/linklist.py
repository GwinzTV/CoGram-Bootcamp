'''
This library seamlessly allows you to create singly linked lists!!!
I have made sure to make this library and its methods easy to understand by adding
comments and descriptive notes where I can. I hope you find ease in its use!

        ==============================
        |==       DEVELOPER:       ==|
        |==    Joshua Iyinkanmi    ==|
        ==============================
'''

# private node for building a singly linked list
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    '''
    This linked list class contains a variety of standard list manipulation/querying methods
    to suit your needs and make the idea of creating a singly linked list a simple reality!
    '''
    def __init__(self):
        self.head = None
        self._length_list = 0

    def __str__(self):
        '''
        Returns the string representation of the linked list.
        '''
        current = self.head
        linked_list = []
        while current:
            linked_list.append(str(current.data))
            current = current.next
        return ' --> '.join(linked_list)

    def prepend(self, data):
        '''
        Adds a new node to the beginning of the linked list.
        '''
        new_node = _Node(data)
        new_node.next = self.head
        self.head = new_node
        self._length_list += 1

    def append(self, data):
        '''
        Adds a node to the end of the linked list.
        '''
        new_node = _Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self._length_list += 1

    def delete(self, data):
        '''
        Deletes a node with the given data from the list.
        Raises ValueError if the data is not found.
        '''
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self._length_list -= 1
                return data
            prev = current
            current = current.next
        raise ValueError(f'{data} is not in the linked list!')

    def search(self, value):
        '''
        Searches for a value in the linked list and returns its index.
        Returns -1 if the value is not found.
        '''
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def is_empty(self):
        '''
        Checks if the linked list is empty.
        '''
        return self.head is None

    def size(self):
        '''
        Returns the size of the linked list.
        '''
        return self._length_list
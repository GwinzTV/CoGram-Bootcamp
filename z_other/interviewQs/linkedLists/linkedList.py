'''
we are going to createt a linked list here and define functions that append, prepend, delete, and insert nodes
'''
# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:
    def __init__ (self):
        self.head = None


    # add a node to the end of the linked list
    def append(self, data):
        # creating new node
        new_node = Node(data)
        # if no nodes in the list, assign new node to head
        if not self.head:
            self.head = new_node
            return
        # assign last node to head for next operation
        last_node = self.head
        # go through the linked list until the last element's pointer is 'None'
        while last_node.next:
            last_node = last_node.next
        # when you reach the last element, add a pointer from the last element to the new node
        last_node.next = new_node


    # add a node to the beginning of the linked list
    def prepend(self, data):
        # create new node
        new_node = Node(data)
        # set the new node's next pointer to the current head
        new_node.next = self.head
        # set the new node as the head of the linked list
        self.head = new_node

    
    def delete(self, data):
        # start at the beginning of the linked list
        current_node = self.head
        # if there is a head node and the data in the node matches data we want to delete, remove the head node
        if current_node and current_node.data == data:
            # set next node as the head node
            self.head = current_node.next
            # current node is set to None, deleted
            current_node = None
            return

        # initialising prev variable
        prev = None
        # iterate through the linked list until end of list is reached, or data is found
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return f'{data} not in linked list!'
        
        # set the previous node's next pointer to the current node's next pointer
        prev.next = current_node.next
        # set current node to None, deletion
        current_node = None

    
    def print_list(self):
        current_node = self.head
        llstr = ''
        while current_node:
            llstr += str(current_node.data) + ' --> '
            current_node = current_node.next
        print(llstr[0:-5])


def main():
    ll = LinkedList()
    sample_data = [1,2,3,4,5,6]
    for data in sample_data:
        ll.append(data)
    ll.print_list()



if __name__ == "__main__":
    main()
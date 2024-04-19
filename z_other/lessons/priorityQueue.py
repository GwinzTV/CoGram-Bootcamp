'''
Common uses of Priority Queues:
 - Dijkstra's Shortest Path Algorithm
 - Data Compression
 - Artificial Intelligence
 - Load Balancing in OSs
 - Optimisation Problems
 - Robotics
 - Medical Systems
 - Event-driven Simulations

    #########################################
    #   Complexities (List implementation)  #   Enqueue -> time: O(n) because each element's priority must be checked and compared.
    #---------------------------------------#   Dequeue -> time: O(1) because pointer is updated or last element is removed.
    # Enqueue:           |   Dequeue:       #
    #  - space: O(1)     |    - space: O(1) #
    #  - time: O(n)      |    - time: O(1)  #
    #########################################

    ##########################################
    # Complexities (Library implementation)  #   Enqueue -> time: O(log n) because adding node to heap.
    #----------------------------------------#   Dequeue -> time: O(log n) because removing node from heap.
    # Enqueue:          |  Dequeue:          #
    #  - space: O(1)    |   - space: O(1)    #
    #  - time: O(log n) |   - time: O(log n) #
    ##########################################
'''

import random as r

class PriorityQueueList:
    def __init__(self):
        self.pqueue = []

    # multiplied priority by -1 because the lowest
    # negative is considered the highest priority.
    def enqueue(self, value, priority):
        self.pqueue.append((-1*priority,value)) 
        self.pqueue.sort()
    

    def dequeue(self):
        if len(self.pqueue) == 0:
            print("Error: Queue Underflow!")
            return
        removed = self.pqueue.pop()
        return removed
    
# implementing the same as above but this time using the library instead, so that we can compare the complexities
import queue

class PriorityQueueLibrary:
    def __init__(self):
        self.pqueue = queue.PriorityQueue()

    # multiplied priority by -1 because the lowest
    # negative is considered the highest priority.
    def enqueue(self, priority, value):
        self.pqueue.put((-1*priority, value))


    def dequeue(self):
        if self.pqueue.qsize() == 0:
            print("Error: Priority Queue Underflow!")
            return None
        else:
            return self.pqueue.get()[1]



def main():
    pque = PriorityQueueList()
    print(pque.pqueue)
    for i in range(5):
        priority = r.randint(1, 20)
        pque.enqueue(i, priority)
        print(pque.pqueue)
    for i in range(5):
        pque.dequeue()
        print(pque.pqueue)



if __name__ == "__main__":
    main()
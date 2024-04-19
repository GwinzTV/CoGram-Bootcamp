'''
Common uses of Queues:
 - Task Scheduling
 - Resource Allocation
 - Network Protocols
 - Printing Queues
 - Web Servers
 - Breath-First Search

    #########################################
    #             Complexities              #
    #---------------------------------------#
    # Enqueue:           |   Dequeue:       #
    #  - space: O(1)     |    - space: O(1) #
    #  - time: O(1)      |    - time: O(1)  #
    #########################################
'''

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()


    def enqueue(self, value):
        self.queue.append(value)


    def dequeue(self):
        if len(self.queue) == 0:
            print("Error: Queue Underflow!")
            return None
        else:
            return self.queue.popleft()


def main():
    que = Queue()
    for i in range(5):
        que.enqueue(i)
        print(que.queue)
    for i in range(5):
        que.dequeue()
        print(que.queue)



if __name__ == "__main__":
    main()
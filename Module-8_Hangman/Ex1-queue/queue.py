#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
queue.py creates a queue which can dequeue and enqueue
Dani van Enk, 11823526
"""

# imported modules
import time

class Queue:
    """
    defines a queue

    methods:
    enqueue() - appends an item to the queue;
    dequeue() - returns the first item in the queue and removes it;
    peek() - returns the first item in the queue;
    size() - returns the size of the queue;
    empty() - empties the queue
    """

    def __init__(self):
        """
        initializes the Queue class
        """

        self._data = []

    def enqueue(self, item):
        """
        adds an item to the end of the queue

        parameters:
        item - to be added item
        """

        self._data.append(item)

    def dequeue(self):
        """
        removes the first item in the queue

        gives error when queue is empty

        returns the removed item
        """

        assert self.size() > 0
        return self._data.pop(0)

    def peek(self):
        """
        gives first in queue

        gives error when queue is empty

        returns the first item in the queue
        """

        assert self.size() > 0
        return self._data[0]

    def size(self):
        """
        returns the size of the queue
        """

        return len(self._data)

    def empty(self):
        """
        empties the queue
        """

        self._data.clear()


def main():
    """
    create queue
    """

    # create a queue
    q = Queue()
    
    # fill it with numbers 0 to 99
    for i in range(100):
        q.enqueue(i)

    # get current hour
    current_hour = time.localtime(time.time()).tm_hour

    # empty queue when I'm awake else empty it every second
    if current_hour > 10 or current_hour < 1:
        q.empty
        print("Hey I'm up now, the queue has been emptied")
    else:
        for j in range(q.size()):
            print(f"removed: {q.dequeue()}")
            print(f"next in queue: {q.peek()}")
            time.sleep(1)


# run main
if __name__ == "__main__":
    main()

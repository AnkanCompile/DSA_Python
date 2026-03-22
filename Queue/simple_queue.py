from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def front(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0


my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue: ", my_queue._data)
print("Dequeue: ", my_queue.dequeue())
print("Queue after dequeue: ", my_queue._data)
print("Peek: ", my_queue.front())
print("isEmpty: ", my_queue.is_empty())

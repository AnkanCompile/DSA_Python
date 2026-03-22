from typing import List, Optional


class CircularQueue:
    def __init__(self, k):
        self.q: List[Optional[int]] = [None] * k
        self.head = self.tail = -1
        self.size = k

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return (self.tail + 1) % self.size == self.head

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        if self.is_empty():
            self.head = self.tail = 0
        else:
            self.head = (self.head - 1 + self.size) % self.size
        self.q[self.head] = value
        return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        if self.is_empty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        self.q[self.tail] = value
        return True

    def delete_front(self):
        if self.is_empty():
            return None
        removed_val = self.q[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return removed_val

    def delete_last(self):
        if self.is_empty():
            return None
        removed_val = self.q[self.tail]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.tail = (self.tail - 1 + self.size) % self.size
        return removed_val

    def front(self):
        if self.head == -1:
            return -1
        return self.q[self.head]

    def rear(self):
        if self.tail == -1:
            return -1
        return self.q[self.tail]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        elements = []
        curr = self.head
        while True:
            elements.append(self.q[curr])
            if curr == self.tail:
                break
            curr = (curr + 1) % self.size
        return elements


my_queue = CircularQueue(5)

my_queue.insert_front(2)
my_queue.insert_front(1)
my_queue.insert_last(3)
my_queue.insert_last(4)
my_queue.insert_last(5)

print("Queue:", my_queue.display())
print("Dequeue Front:", my_queue.delete_front())
print("Dequeue Rear:", my_queue.delete_last())
print("Queue after dequeue:", my_queue.display())
print("Queue front:", my_queue.front())
print("Queue back:", my_queue.rear())

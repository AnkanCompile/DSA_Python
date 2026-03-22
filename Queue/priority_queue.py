import heapq
from typing import List, Tuple


class PriorityQueue:
    def __init__(self):
        self.heap: List[Tuple[int, str]] = []

    def push(self, task: str, priority: int):
        heapq.heappush(self.heap, (-priority, task))
        print(f"Inserted: {task} (priority {priority})")

    def pop(self):
        if not self.heap:
            print("Queue is empty")
            return None
        priority, task = heapq.heappop(self.heap)
        print(f"Removed: {task} (priority {-priority})")
        return task

    def display(self):
        print("Current Queue:")
        for pri, task in self.heap:
            print(f"{task} (priority {-pri})")
        print()


pq = PriorityQueue()

pq.push("Eat", 1)
pq.push("Study", 5)
pq.push("Sleep", 2)

pq.display()

pq.pop()
pq.pop()
pq.pop()

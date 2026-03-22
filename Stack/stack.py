class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack: ", my_stack.stack)
print("Pop: ", my_stack.pop())
print("Stack after Pop: ", my_stack.stack)
print("Peek: ", my_stack.peek())
print("isEmpty: ", my_stack.is_empty())
print("Size: ", my_stack.size())

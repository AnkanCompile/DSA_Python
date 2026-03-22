class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node


def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def delete_at_beginning(head):
    if head is None:
        print("Error: Singly linked list is empty")
        return None
    new_head = head.next
    del head
    return new_head


def delete_after_node(node):
    if node is None or node.next is None:
        print("Error: The given node is None or the next node is None")
        return
    next_node = node.next
    node.next = next_node.next
    del next_node


def delete_at_end(head):
    if head is None or head.next is None:
        print("Error: Singly linked list is empty or has only one node")
        return None
    current = head
    while current.next.next:
        current = current.next
    del_node = current.next
    current.next = None
    del del_node
    return head


def reverse(head):
    prev, curr = None, head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def traverse(head):
    current = head
    while current:
        print(str(current.data) + " -> ", end=" ")
        current = current.next
    print("None")


head = None
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 1)
insert_after_node(head, 2)
insert_after_node(head, 5)
head = insert_at_beginning(head, 0)
insert_at_end(head, 4)
head = delete_at_beginning(head)
delete_after_node(head)
head = delete_at_end(head)
head = reverse(head)

traverse(head)

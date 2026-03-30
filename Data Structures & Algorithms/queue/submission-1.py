class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0


    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        new_val = Node(value)
        new_val.next = self.tail
        new_val.prev = self.tail.prev
        self.tail.prev.next = new_val
        self.tail.prev = new_val
        self.length += 1

    def appendleft(self, value: int) -> None:
        new_val = Node(value)
        new_val.prev = self.head
        new_val.next = self.head.next
        self.head.next.prev = new_val
        self.head.next = new_val 
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        elif self.length == 1:
            value = self.head.next.val
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length -= 1
            return value

        else:
            value = self.tail.prev
            value.prev.next = self.tail
            self.tail.prev = value.prev 
            self.length -= 1
            return value.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        elif self.length == 1:
            value = self.head.next.val
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length -= 1
            return value

        else:
            value = self.head.next
            self.head.next = value.next
            value.next.prev = self.head 
            self.length -= 1
            return value.val


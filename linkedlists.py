class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = SLLNode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_mid(self, data, pos):
        if pos <= 1 or self.head is None:
            self.insert_front(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp.next is None:
                break
            temp = temp.next
        new_node = SLLNode(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_mid(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos <= 1:
            self.delete_front()
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = DLLNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = DLLNode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_mid(self, data, pos):
        if pos <= 1 or self.head is None:
            self.insert_front(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp.next is None:
                break
            temp = temp.next
        new_node = DLLNode(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_mid(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos <= 1:
            self.delete_front()
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


class CLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = CLLNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = CLLNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_mid(self, data, pos):
        if pos <= 1 or self.head is None:
            self.insert_front(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp.next == self.head:
                break
            temp = temp.next
        new_node = CLLNode(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def delete_mid(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos <= 1:
            self.delete_front()
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp.next == self.head:
                print("Invalid position")
                return
            temp = temp.next
        if temp.next == self.head:
            print("Invalid position")
            return
        temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


sll = SLL()
dll = DLL()
cll = CLL()

sll.insert_front(20)
sll.insert_end(40)
sll.insert_mid(30, 2)
sll.display()
sll.delete_mid(2)
sll.display()

dll.insert_front(20)
dll.insert_end(40)
dll.insert_mid(30, 2)
dll.display()
dll.delete_mid(2)
dll.display()

cll.insert_front(20)
cll.insert_end(40)
cll.insert_mid(30, 2)
cll.display()
cll.delete_mid(2)
cll.display()
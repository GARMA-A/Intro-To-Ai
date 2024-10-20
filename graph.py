class Node:
    data: int
    next: "Node"

    def __init__(self):
        self.data = 0
        self.next = None


class Stack:
    head: "Node"

    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def push(self, val: int):
        if self.head is None:
            self.head = Node()
            self.head.data = val
        else:
            temp = Node()
            temp.data = val
            temp.next = self.head
            self.head = temp

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


class queue:
    front: "Node"
    tail: "Node"

    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self, val: int):
        if self.front is None:
            self.front = Node()
            self.front.data = val
            self.tail = self.front
        else:
            temp = Node()
            temp.data = val
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data


def main():

    mystack = Stack()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.display()


if __name__ == "__main__":
    main()

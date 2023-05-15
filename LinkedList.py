class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

    def __str__(self):
        return self.data


class LinkedList:
    @staticmethod
    def defaultComparator(a, b):
        return b >= a

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.nextE
        return "[" + ", ".join(result) + "]"

    def get(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return

        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return

        current = self.head
        while current.nextE is not None:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                self.size -= 1
                return
            current = current.nextE

    def add_node(self, value, func=None):
        new_element = Element(value)

        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size = 1
            return

        if func is None:
            func = LinkedList.defaultComparator

        current = self.head
        previous = None
        while current is not None and func(current.data, value):
            previous = current
            current = current.nextE

        if previous is None:
            new_element.nextE = self.head
            self.head = new_element
        elif current is None:
            self.tail.nextE = new_element
            self.tail = new_element
        else:
            previous.nextE = new_element
            new_element.nextE = current

        self.size += 1

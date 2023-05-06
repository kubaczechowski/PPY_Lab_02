class Element:
    # metoda jest wywoływana zawsze jak tworzymy nowy obiekt
    # if the argument is not provided we set default values
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.nextE
        return '->'.join(result)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        previous = None
        while current:
            if current.data == e:
                if previous:
                    previous.nextE = current.nextE
                else:
                    self.head = current.nextE
                self.size -= 1
                return
            previous = current
            current = current.nextE

    def append(self, e, func=None):
        new_node = Element(e)
        self.tail = new_node
        if not self.head:
            self.head = new_node
        else:
            if not func:
                func = lambda a, b: a >= b
            current = self.head
            previous = None
            while current and func(current.data, e):
                previous = current
                current = current.nextE
            if previous:
                previous.nextE = new_node
            else:
                self.head = new_node
            new_node.nextE = current
        self.size += 1

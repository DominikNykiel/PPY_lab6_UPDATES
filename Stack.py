class Stos:
    def __init__(self, max_size):
        self.stack = list()
        self.max_size = max_size

    def put(self, element):
        if len(self.stack) < self.max_size:
            self.stack.append(element)
        else:
            print("error")

    def putUpgrade(self, *element):
        for element in element:
            if len(self.stack) < self.max_size:
                self.stack.append(element)
            else:
                print("error")
                return

    def __str__(self):
        return f"Stack: {','.join(self.stack)} \n Size: {self.max_size}"

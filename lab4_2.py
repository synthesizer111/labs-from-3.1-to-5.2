class Stack:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        for value in values:
            self.items.append(value)

    def copy(self):
        new_stack = Stack()
        new_stack.items = self.items.copy()
        return new_stack

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def extend(self, stack):
        while not stack.is_empty():
            self.append(stack.pop())

    def next(self):
        new_stack = self.copy()
        new_stack.pop()
        return new_stack

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def clear(self):
        self.items = []

    def __add__(self, other):
        new_stack = Stack()
        new_stack.extend(self)
        new_stack.extend(other)
        return new_stack

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        for i in range(self.size()):
            if self.items[i] != other.items[i]:
                return False
        return True

    def __rshift__(self, N):
        new_stack = self.copy()
        for i in range(N):
            new_stack.pop()
        return new_stack

    def __str__(self):
        if self.is_empty():
            return "[]"
        stack_str = "["
        for i in range(self.size()-1, -1, -1):
            stack_str += str(self.items[i])
            if i != 0:
                stack_str += " -> "
        stack_str += "]"
        return stack_str

    def __next__(self):
        return self.next()
s1 = Stack(1, 2, 3)
print(s1)
s1.append(4, 5)
print(s1)
s2 = s1.copy()
sx = s1.copy()
print(sx.pop())
print(sx)
print(s2)
print(s1 == s2, id(s1) == id(s2))
s3 = s2.next()
print(s1, s2, s3, sep = '\n')
print(s1 + s3)
s3.extend(Stack(1, 2))
print(s3)
s4 = Stack(1, 2)
s4 += s3 >> 4
print(s4)
s5 = next(s4)
print(s4)
print(s5)
s6 = s5.next()
print(s4, s5, s6, sep = '\n')
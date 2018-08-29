class stacks():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        t = self.stack[-1]
        del self.stack[-1]
        return t

    def peek(self):
        t = self.stack[-1]
        return t

    def size1(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []

st = stacks()
st.push(2)
st.push(5)
st.push(6)
st.push(4)
print(st.pop())
print(st.stack)

class Queue():
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        t = self.queue[0]
        del self.queue[0]
        return t

    def peek(self):
        t = self.queue[0]
        return t

    def size1(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []

q = Queue()
q.push(2)
q.push(5)
q.push(6)
q.push(4)
print(q.pop())
print(q.queue)

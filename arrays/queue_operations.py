class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)  # This 0 makes it a Queue as it returns the very first element from an array!

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)


myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

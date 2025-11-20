class Stack:
    def __init__(self):
        self.stack = []


    # push - ask user for input value to insert or push into stack
    def push(self, val):
        self.stack.append(val)

    # isEmpty -  check if the stack is empty
    def isEmpty(self):
        return bool (len(self.stack) == 0)
    # pop - Removes and return the top / last element from the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    # peek - returns the top or last element fromt the stack
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# create a stack class object here:

s1 = Stack()
print("is stack empty: ",s1.isEmpty())
print("get the last element: ",s1.peek())
print("remove the last element: ",s1.pop())
print(s1.stack)
s1.push(1)
print(s1.stack)
print("is stack empty: ",s1.isEmpty())
print("get the last element: ",s1.peek())
print("remove the last element: ",s1.pop())
print(s1.stack)


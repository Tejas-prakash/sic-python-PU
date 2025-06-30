stack = []

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
    return "Stack is empty"

def peek():
    if not is_empty():
        return stack[-1]
    return "Stack is empty"

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

push(10)
push(20)
push(30)
print(pop())    
print(peek())   
print(size())   

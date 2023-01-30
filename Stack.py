class Stack():
  def __init__(self):
    #Initialises a empty list in the memory, we can import this class in srpn.py and make it an object, this allows
    #for us to have methods that closely resemble the behaviour of a stack
    self.stack = []
  
  def push(self, item):
    self.stack.append(item)

  def pop(self):
    #Stores item at the top of the list, removes the top index and returns item
    item = self.stack[-1]
    self.stack.pop(-1)
    return item
  
  def peek(self):
    return self.stack[-1]

  def is_underflow(self, length):
    #Returns true if the stack is <= a given length
    return (len(self.stack) <= length)

  def is_overflow(self):
    #Returns true if number of items in the stack is greater than 22
    return len(self.stack) > 22
  
  def view_stack(self):
    return self.stack
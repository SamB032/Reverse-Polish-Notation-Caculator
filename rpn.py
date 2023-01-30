import Stack

class UserInput():
  #maximum and minimum a given integer can be
  MIN_VALUE = -2147483648
  MAX_VALUE = 2147483647
  RANDOM_LIST = [
    1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335,
    719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027,
    783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426,
    304089172, 1303455736, 35005211, 521595368, 1804289383
  ]  #Stores the the list of random values in storage

  def __init__(self):
    self.stack = Stack.Stack()  #Initaites the stack class as a object
    self.random_pointer = 0  #Used to point to the next random number in the list

  def process_command(self, command):
    if command.lstrip('-').isdigit():
      #Checks to see if adding the digit will cause the stack to overflow, else push it to the stack
      if self.stack.is_overflow():
        print('Stack overflow.')
      else:
        self.stack.push(str(self.limit_value(int(command))))

    elif command in "+*-%":
      #Checks command is +, *, - or % and calls function passing it as the parameter.
      self.caculate(command)

    elif command == "^":
      #Calls the caculate_pow function if command contains a exponent,
      #we need additional checks for exponents in rpn
      self.caculate_pow()

    elif command == '/':
      #Passes "//" as parameter to caculate method, becuase rpn preforms a integer division
      self.caculate('//')

    elif command == "=":
      #Checks to see if the queue is empty, we print a message and push the min value, else we call the peek method
      if self.stack.is_underflow(0):
        print("Stack empty.")
        self.stack.push(str(UserInput.MIN_VALUE))
      else:
        print(self.stack.peek())

    elif command == 'd':
      #if the stack is empty, the program will print MIN_VALUE, else prints out all values on the stack
      if self.stack.is_underflow(0):
        print(UserInput.MIN_VALUE)
      else:
        self.display_stack()

    elif command == " ":
      pass

    # Checks to see if the user an given a float, this will give a error message
    # and push each side of the decimal as its own number
    elif command.lstrip('-').replace(".", "").isdigit():
      number_split = command.split(".")
      generate_error_message(".")
      self.stack.push(number_split[0])
      self.stack.push(number_split[1])

    elif command == "r":
      #Calls the random number method
      if self.stack.is_overflow():
        print('Stack overflow.')
      else:
        self.find_random_number()
    else:
      generate_error_message(command)

  def caculate(self, operation):
    #Takes input in the form of an opertation. Pops the two items from the stack, carries out the
    #caculation and pushs it back on the Stack. if length of stack is <= 1, prints stack underflow instead
    if not self.stack.is_underflow(1):
      try:
        right_val = self.stack.pop()
        left_val = self.stack.pop()
        number = eval(left_val + operation + right_val)
        self.stack.push(str(self.limit_value(number)))
      except ZeroDivisionError:
        print("Divide by 0.")
        self.stack.push("0")
    else:
      print("Stack underflow.")

  def caculate_pow(self):
    #Cacaultes the Exponent of a number. prints message if exponent is negative. Turns min number
    # to max number is base is negtive. Pushes the result of the cacaulation to the stack
    right_val = self.stack.pop()
    left_val = self.stack.pop()
    if int(right_val) < 0:
      print("Negative power.")
      self.stack.push(left_val)
      self.stack.push(right_val)
    else:
      number = self.limit_value(eval(left_val + "**" + right_val))
      if number == UserInput.MIN_VALUE:
        number = UserInput.MAX_VALUE
      self.stack.push(str(number))

  def find_random_number(self):
    self.stack.push(str(UserInput.RANDOM_LIST[self.random_pointer]))  #Find the number at the index and push it to stack
    if self.random_pointer == 23:  #Resets random_pointer to 0 if its == 23 else increments it by 1
      self.random_pointer = 0
    else:
      self.random_pointer += 1

  def display_stack(self):
    #Iterates through the stack, prints each value on a new line
    for value in self.stack.view_stack():
      print(value)

  def limit_value(self, number):
    #Limits the maximum and minimum value of a number that is given as the parameter, then returns the number
    #The original program in C stored values as a long
    return max(min(UserInput.MAX_VALUE, number), UserInput.MIN_VALUE)

def generate_error_message(command):
  #Generates an error message for each letter in the command and prints it to the screen
  for char in command:
    print(f'Unrecognised operator or operand "{char}".')

def remove_comments(expression):
  #Removes strings that are contained within #___# block
  if "#" in expression:
    for i in range(int(expression.count("#") / 2)):
      start = expression.index("#")  #Stores the index of the first # starting from left
      expression.pop(start)
      end = expression.index("#")  #Stores the index of the next # starting from left
      expression.pop(end)
      del (expression[start:end])  #Deletes the # block from the list
  return expression

if __name__ == "__main__":
  user_input = UserInput()
  while True:
    try:
      #Prompts for user input, splits the input, removes the comments and calls the process_command method
      expression = input()
      expression = remove_comments(expression.split())
      for char in expression:
        pc = user_input.process_command(char)
    except EOFError:
      exit()

STCKR_CLEAR = "clear"
STCKR_PUSH = "push"
STCKR_PRINT = "print"
STCKR_DUMP = "dump"
STCKR_PLUS = "plus"
STCKR_MINUS = "minus"
STCKR_MULT = "mult"
STCKR_DIV = "div"

class stackr():
    def __init__(self):
        self.stack = []

    def run_command(self, command):
        if STCKR_CLEAR in command:
            self.stack = []
        elif STCKR_PUSH in command: # adds new value to the top of the stack 
            self.stack.append(command[command.find("(") + 1:command.find(")")])
        elif STCKR_PRINT in command: # prints whole stack
            print(self.stack)
        elif STCKR_DUMP in command: # prints first value in stack
            a = self.stack.pop()
            print(a)
        elif STCKR_PLUS in command: # adds top two values of the stack and puts the result to top of stack
            a = int(self.stack.pop())
            b = int(self.stack.pop())
            self.stack.append(a + b)
        elif STCKR_MINUS in command: # subtracts top two values of the stack and puts the result to top of stack
            a = int(self.stack.pop())
            b = int(self.stack.pop())
            self.stack.append(a - b)
        elif STCKR_MULT in command:
            a = int(self.stack.pop())
            b = int(self.stack.pop())
            self.stack.append(a * b)
        elif STCKR_DIV in command:
            a = int(self.stack.pop())
            b = int(self.stack.pop())
            self.stack.append(a / b)
        else:
            print("COMMAND NOT RECOGNIZED:", command)
            return
            #test
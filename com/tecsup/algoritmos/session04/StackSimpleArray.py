'''
Created on Mar 11, 2019
@author: jgomezm
'''
class StackSimpleArray(object):

    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def size(self):
        return len(self.stk)

    def push(self, item):
        if len(self.stk) >= self.limit:
            print('Stack Overflow!')
        else:
            self.stk.append(item)
            print('Stack after Push', self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) < 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk[-1]

# Execution
our_stack = StackSimpleArray(5)
our_stack.push('1')
our_stack.push('21')
our_stack.push('14')
our_stack.push('31')
our_stack.push('19')
our_stack.push('3')
our_stack.push('99')
our_stack.push('9')

print( our_stack.size())
print( our_stack.peek())
print( our_stack.pop())
print( our_stack.peek())
print( our_stack.pop())
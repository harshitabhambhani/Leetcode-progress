class MyQueue(object):

    def __init__(self):
        self.stack1 = []  # Main stack
        self.stack2 = []  # Temporary stack for reversing elements

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack2:
            self._transfer()
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            self._transfer()
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2

    def _transfer(self):
        """
        Transfer elements from stack1 to stack2 to reverse the order.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())  # Output: 1
print(obj.pop())   # Output: 1
print(obj.empty()) # Output: False

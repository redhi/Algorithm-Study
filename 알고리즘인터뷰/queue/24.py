'''
24. 스택을 이용한 큐 구현
leetcode 232. Implement Queue using Stacks
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        value = self.s[0]
        self.s.remove(value)
        return value

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if (len(self.s) == 0):
            return True
        else:
            return False

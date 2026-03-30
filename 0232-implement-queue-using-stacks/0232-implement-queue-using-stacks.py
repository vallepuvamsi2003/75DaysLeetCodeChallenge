class MyQueue:

    def __init__(self):
        self.input = []   # stack for push
        self.output = []  # stack for pop/peek

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # ensure output stack has elements
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            # Move elements from input → output
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output
class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []

    def push(self, item: int) -> None:
        self.stack.append(item)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def __repr__(self) -> str:
        return f"Stack({self.stack})"
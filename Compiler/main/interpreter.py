from compiler import *
memory = MemoryManager()
stack = Stack()
class Interpreter:
    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.bytecode = bytecode
        self.ptr: int = 0
    def interpret(self) -> None:
        """Interprets the bytecode."""
        for bc in self.bytecode:
            if bc.type == BytecodeType.DECLARE_VAR:
                memory.add(bc.value,stack.pop())
            elif bc.type == BytecodeType.PUSH:
                stack.push(bc.value)
            elif bc.type == BytecodeType.PRINT:
                if memory.ismemexists(bc.value):
                    print(memory.get(bc.value))
                else:
                    raise Exception(f"Variable Value Not Found: {bc.value}")
        # print(self.stack)
        # print(repr(memory))
        
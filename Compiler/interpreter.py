from compiler import *
class Interpreter:
    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.bytecode = bytecode
        self.ptr: int = 0
    def interpret(self) -> None:
        """Interprets the bytecode."""
        for bc in self.bytecode:
            if bc.type == BytecodeType.DECLARE_VAR:
                current_var = Memory(bc.value, None)
            elif bc.type == BytecodeType.PUSH:
                stack.push(bc.value)
            elif bc.type == BytecodeType.STORE_VAR:
                current_var.value = stack.pop()
                memory.add(current_var.name, current_var.value)
                if current_var.value is None:
                    raise RuntimeError(f"Variable {bc.value!r} not declared.")
            elif bc.type == BytecodeType.PRINT:
                print(stack.pop())
        # print(self.stack)
        # print(repr(memory))
        
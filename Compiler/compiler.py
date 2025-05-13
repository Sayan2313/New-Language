from dataclasses import dataclass
from enum import StrEnum,auto
from typing import Any, Generator
from parser import *
from stack import *
from memory import *
memory = MemoryManager()
stack = Stack()
class BytecodeType(StrEnum):
    BINOP = auto()
    PUSH = auto()
    POP = auto()
    DECLARE_VAR = auto()
    STORE_VAR = auto()
    PRINT = auto()
@dataclass
class Bytecode:
    type: BytecodeType
    value: Any = None
class Compiler:
    def __init__(self, tree: TreeNode) -> None:
        self.tree = tree
    def compile(self)->Generator[Bytecode, None, None]:
        """Compiles the AST into bytecode."""
        match self.tree:
            case Declaration(identifier, value):
                yield Bytecode(BytecodeType.DECLARE_VAR, identifier)
                yield Bytecode(BytecodeType.PUSH, value)
                yield Bytecode(BytecodeType.STORE_VAR, identifier)
            case Print(value):
                if isinstance(value, str):
                    if not memory.ismemexists(value):
                        raise RuntimeError(f"Variable {value!r} not declared.")
                    yield Bytecode(BytecodeType.PUSH, memory.get(value))
                else:
                    yield Bytecode(BytecodeType.PUSH, int(value))
                yield Bytecode(BytecodeType.PRINT)
            # case BinOp(op, left, right):
            #     yield from self.compile(left)
            #     yield from self.compile(right)
            #     yield Bytecode(BytecodeType.BINOP, op)
            # case Int(value):
            #     yield Bytecode(BytecodeType.PUSH, value.value)
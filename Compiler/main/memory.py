from dataclasses import dataclass
@dataclass
class Memory():
    name : str
    value : int = -999999
    def __repr__(self):
        return f"Memory({self.name}, {self.value})"
class MemoryManager():
    def __init__(self) -> None:
        self.memory : dict[str,Memory] = {}
    def add(self, name : str, value : int) -> None:
        self.memory[name] = Memory(name, value)
    def get(self, name : str) -> int:
        if name in self.memory:
            return self.memory[name].value
        raise RuntimeError(f"Variable {name} not found.")
    def set(self, name : str, value : int) -> None:
        if name in self.memory:
            self.memory[name].value = value
        raise RuntimeError(f"Variable {name} not found.")
    def ismemexists(self, name : str) -> bool:
        if name in self.memory:
            return True
        return False
    def __repr__(self):
        st = "MemoryManager("
        for mem in self.memory:
            st += "(" + str(mem) + ", " + str(self.memory[mem].value) + "), " 
        st += ")"
        return st
        
        
"""
This is the main file for the Compiler project.
It will take a file name as input and interpret the code in it.
"""
from lex import *
from parser import *
from compiler import *
from interpreter import *
from memory import *
import sys
def interpret_code(code):
    tokenizer = Tokenizer(code)
    # for token in tokenizer:
    #     print(token)
    parser = Parser(list(tokenizer))
    # print(parser.parse()) 
    compiler = Compiler(parser.parse())
    # for bc in compiler.compile():
    #     print(bc)
    interpreter = Interpreter(compiler.compile())
    interpreter.interpret()
if __name__ == "__main__":
    lines : list[str] = []
    if len(sys.argv) < 2:
        print("Please provide a file name to interpret")
        exit(1)
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
        # print(lines)
    for line in lines:
        # print(line)
        interpret_code(line)

    
    
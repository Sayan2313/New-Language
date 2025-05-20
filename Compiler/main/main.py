"""
This is the main file for the Compiler project.
It will take a file name as input and interpret the code in it.
Language: Sayan
Version: 1.0.0.1
"""
from io import SEEK_SET
from tokenizer import *
from parser import *
from compiler import *
from interpreter import *
from memory import *
from grammer import *
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
    interpreter = Interpreter(list(compiler.compile()))
    interpreter.interpret()
if __name__ == "__main__":
    # getSteps("src/Main.txt","src/output.txt")
    lines : list[str] = []
    start_index = 0
    end_index = start_index
    if len(sys.argv) < 2:
        print("Please provide a file name to interpret")
        exit(1)
    with open(sys.argv[1], "r") as f:
        s = ""
        for l in f.readlines():
            l = l.removesuffix("\n")
            if l.endswith(";"):
                s+=l
                lines.append(s.strip())
                s = ""
            else:
                s+=l
    # print(lines)
    #Run the Program
    program_counter = 0
    while program_counter < len(lines):
        current_line : list[str] = []
        current_line.append(lines[program_counter])
        # if current_line[-1].startswith('jodi'):
    #         while True:
    #             program_counter += 1
    #             current_line.append(lines[program_counter])
    #             if current_line[-1].endswith('ses jodi'):
    #                 break
    #     if current_line[-1].endswith('jodi'):
    #         print(current_line)
    #         # interpret_code(line)
    #     else:
        # print(current_line[-1].split())
        interpret_code(current_line[-1].split())
        program_counter += 1
    

    
    
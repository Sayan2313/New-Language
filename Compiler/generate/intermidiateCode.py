from Compiler.main.tokenizer import *
from Compiler.main.parser import *
from Compiler.main.compiler import *
def getSteps(filename: str,output: str):
    lines : list[str] = []
    with open(filename, "r") as f:
        s = ""
        for l in f.readlines():
            l = l.removesuffix("\n")
            if l.endswith(";"):
                s+=l
                lines.append(s.strip())
                s = ""
            else:
                s+=l
    with open(output, "w+") as f:
        program_counter = 0
        listofparser : list[TreeNode] = []
        listofbytecodes : list[Bytecode] = []
        listofTokens : list[list[Token]] = []
        countToken =  0
        while program_counter < len(lines):
            current_line : list[str] = []
            current_line.append(lines[program_counter])
            tokenizer = Tokenizer(current_line[-1].split())
            current_tokens = []
            for token in tokenizer:
                current_tokens.append(token)
                countToken+=1
            listofTokens.append(current_tokens)
            parser = Parser(current_tokens)
            listofparser.append(parser.parse())
            compiler = Compiler(parser.parse())
            for bc in list(compiler.compile()):
                listofbytecodes.append(bc)
            program_counter += 1
        f.write(f"1. Tokens({countToken}):- " + "\n")
        for tokens in listofTokens:
            for token in tokens:
                f.write(str(token) + "\n")
        f.write(f"2. ParserTrees({len(listofparser)}):- " + "\n")
        for tree in listofparser:
            f.write(str(tree) + "\n")
        f.write(f"3. ByteCodes({(len(listofbytecodes))}):- " + "\n")
        for bc in listofbytecodes:
            f.write(str(bc) + "\n")
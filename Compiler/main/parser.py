from dataclasses import dataclass
from tokenizer import *
@dataclass
class TreeNode:
    pass
@dataclass
class BinOp(TreeNode):
    op: str
    left: int
    right: int
@dataclass
class Declaration(TreeNode):
    identifier: str
    value: Any
@dataclass
class Print(TreeNode):
    value: Any
class Parser:
    def __init__(self, tokens : list[Token]) -> None:
        self.tokens = tokens
        self.next_token_index: int = 0
    def eat(self, expected_token_type: TokenType) -> Token:
        next_token = self.tokens[self.next_token_index]
        self.next_token_index += 1
        if next_token.type != expected_token_type:
            raise RuntimeError("Syntax error")
        return next_token
    def peek(self, skip: int = 0) -> TokenType | None:
        peek_at = self.next_token_index + skip
        return self.tokens[peek_at].type if peek_at < len(self.tokens) else None
    def parse(self) -> TreeNode:
        """Parses the program."""
        match self.peek():
            case TokenType.KEYWORD:
                if self.peek(1) == TokenType.IDENTIFIER and self.peek(2) == TokenType.OPERATOR and (self.peek(3) == TokenType.INT or self.peek(3)==TokenType.FLOAT):
                    return self.parse_declaration()
                elif self.peek(1) == TokenType.IDENTIFIER or self.peek(1) == TokenType.INT:
                    return self.parse_print()
        raise RuntimeError("Invalid syntax: Unexpected token sequence")
    def parse_declaration(self) -> Declaration:
        """Parses a variable declaration."""
        self.eat(TokenType.KEYWORD)
        identifier = self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.OPERATOR)
        val = ""
        if self.peek() == TokenType.INT:
            val = str(self.eat(TokenType.INT).value)
        elif self.peek() == TokenType.FLOAT:
            val = str(self.eat(TokenType.FLOAT).value)
        while self.peek() != TokenType.EOF:
            val+=str(self.eat(TokenType.OPERATOR).value)
            val+=str(self.eat(TokenType.INT).value) if self.peek()==TokenType.INT else str(self.eat(TokenType.FLOAT).value)
        self.eat(TokenType.EOF)
        self.next_token_index = 0
        final_value = float(eval(val)) if isinstance(eval(val),float) else int(eval(val))
        return Declaration(identifier.value, final_value)
    def parse_print(self) -> Print:
        """Parses a print statement."""
        self.eat(TokenType.KEYWORD)
        if self.peek() == TokenType.IDENTIFIER:
            identifier = self.eat(TokenType.IDENTIFIER)
        else:
            identifier = self.eat(TokenType.INT) if self.peek()==TokenType.INT else self.eat(TokenType.FLOAT) 
        self.eat(TokenType.EOF)
        self.next_token_index = 0
        return Print(identifier.value)
    
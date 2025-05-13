from dataclasses import dataclass
from lex import *
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
                if self.peek(1) == TokenType.IDENTIFIER and self.peek(2) == TokenType.OPERATOR and self.peek(3) == TokenType.INT:
                    return self.parse_declaration()
                elif self.peek(1) == TokenType.IDENTIFIER or self.peek(1) == TokenType.INT:
                    return self.parse_print()
    def parse_declaration(self) -> Declaration:
        """Parses a variable declaration."""
        self.eat(TokenType.KEYWORD)
        identifier = self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.OPERATOR)
        val = str(self.eat(TokenType.INT).value)
        while self.peek() != TokenType.EOF:
            val+=str(self.eat(TokenType.OPERATOR).value)
            val+=str(self.eat(TokenType.INT).value)
        self.eat(TokenType.EOF)
        self.next_token_index = 0
        return Declaration(identifier.value, int(eval(val)))
    def parse_print(self) -> None:
        """Parses a print statement."""
        self.eat(TokenType.KEYWORD)
        if self.peek() == TokenType.IDENTIFIER:
            identifier = self.eat(TokenType.IDENTIFIER)
        else:
            identifier = self.eat(TokenType.INT)
        self.eat(TokenType.EOF)
        self.next_token_index = 0
        return Print(identifier.value)
    
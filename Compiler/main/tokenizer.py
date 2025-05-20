"""
This module contains the Tokenizer class, which is responsible for tokenizing the input code.
It takes a string of code and breaks it down into tokens, which are then used by the parser to create an abstract syntax tree (AST).
"""
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Generator
from grammer import *
import re
class TokenType(StrEnum):
    INT = auto()
    FLOAT = auto()
    OPERATOR = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    SYMBOLS = auto()
    EOF = auto()
@dataclass
class Token:
    type: TokenType
    value: Any = None
class Tokenizer:
    def __init__(self, code: list[str]) -> None:
        self.code = code
        self.ptr : int = -1
    def next_token(self) -> Token:
        """Returns the next token in the code."""
        self.ptr += 1
        if self.code[self.ptr] == ENDOFLINE:
            return Token(TokenType.EOF,self.code[self.ptr])
        current_token = self.code[self.ptr] 
        if current_token in RESERVED_KEYWORD:
            return Token(TokenType.KEYWORD, current_token)
        elif current_token in ASSIGNMENT_OPERATORS:
            return Token(TokenType.OPERATOR, current_token)
        elif current_token in ARITHMETIC_OPERATORS:
            return Token(TokenType.OPERATOR, current_token)
        elif current_token in SYMBOLS:
            return Token(TokenType.SYMBOLS, current_token)
        elif current_token == "end_if":
            return Token(TokenType.KEYWORD, current_token)
        elif current_token.isalpha():
            return Token(TokenType.IDENTIFIER, current_token)
        elif bool(re.match(INTPATTERN,current_token)):
            return Token(TokenType.INT, int(current_token)) 
        elif bool(re.match(FLOATPATTERN,current_token)):
            return Token(TokenType.FLOAT, float(current_token)) 
        else:
            raise ValueError(f"Syntax Error: {current_token}")
    def __iter__(self) -> Generator[Token, None, None]:
        """Iterates over the tokens in the code."""
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token

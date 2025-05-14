"""
This module contains the Tokenizer class, which is responsible for tokenizing the input code.
It takes a string of code and breaks it down into tokens, which are then used by the parser to create an abstract syntax tree (AST).
"""
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Generator
from grammer import *
class TokenType(StrEnum):
    INT = auto()
    OPERATOR = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    EOF = auto()
@dataclass
class Token:
    type: TokenType
    value: Any = None
class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code.split()
        self.ptr : int = -1
    def next_token(self) -> Token:
        """Returns the next token in the code."""
        self.ptr += 1
        if self.ptr == len(self.code):
            return Token(TokenType.EOF)
        current_token = self.code[self.ptr] 
        if current_token in RESERVED_KEYWORD:
            return Token(TokenType.KEYWORD, current_token)
        elif current_token in ASSIGNMENT_OPERATORS:
            return Token(TokenType.OPERATOR, current_token)
        elif current_token in ARITHMETIC_OPERATORS:
            return Token(TokenType.OPERATOR, current_token)
        elif current_token.isalpha():
            return Token(TokenType.IDENTIFIER, current_token)
        elif current_token.isnumeric():
            return Token(TokenType.INT, int(current_token)) 
        else:
            raise ValueError(f"Unknown token: {current_token}")
    def __iter__(self) -> Generator[Token, None, None]:
        """Iterates over the tokens in the code."""
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token

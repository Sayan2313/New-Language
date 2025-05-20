"""
Language: Bengal
Version: 0.0.1
Author: Sayan
Grammar rules for the My programming language
1)dhori is a keyword for assignment
2)dekhao is a keyword for print
3)cholo is a keyword for loop(not supported yet)
"""
import re
RESERVED_KEYWORD = ['dhori','dekhao','jodi','ses_jodi']
ASSIGNMENT_OPERATORS = ['=']
ARITHMETIC_OPERATORS = ['+', '-', '*', '/']
SYMBOLS = ['(', ')']
INTPATTERN = r"^-?\d+$" 
FLOATPATTERN = r"^-?\d+(\.\d*)?$"
ENDOFLINE = ";"
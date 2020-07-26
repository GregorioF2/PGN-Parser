tokens = (
    'MOVEMENT',
    'LKEY',
    'RKEY',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'TDOTS',
    'DOTS',
    'RESULT',
    'ID'
)

t_LBRACKET = r'\['
t_RBRACKET = r']'

def t_MOVEMENT(t):
    r'([PNBRQK]?[a-h]?[1-8]?x?[a-h][1-8][\+|#]?|O-O-O|O-O)'
    return t
def t_LKEY(t):
    r'{'
    return t
def t_RKEY(t):
    r'}'
    return t

def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t
def t_TDOTS(t):
    r'\d+(\.\.\.)'
    return t
def t_DOTS(t):
    r'\d+\.'
    return t
def t_RESULT(t):
    r'(1-0|0-1)'
    return t

def t_ID(t):
    r'([a-z]|[A-Z]|\d|"|:|-|\.)+'
    return t


# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    return t
    t.lexer.skip(1)

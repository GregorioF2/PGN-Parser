aceptado = True


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


import ply.lex as lex
lexer = lex.lex()

def p_partida(t):
    'partida : metadata movimientos resultado'

def p_metadata(t):
    '''metadata : LBRACKET relleno RBRACKET metadata
                | empty'''

def p_movimientos(t):
    '''movimientos : separador turno movimientos
                   | empty'''

def p_separador(t):
    '''separador : DOTS
                 | TDOTS'''

def p_turno(t):
    'turno : jugada comentario'

def p_jugada(t):
    '''jugada : MOVEMENT
              | MOVEMENT MOVEMENT'''

def p_comentario(t):
    '''comentario : LPAREN turno RPAREN
                  | LKEY turno RKEY
                  | LPAREN relleno RPAREN
                  | LKEY relleno RKEY
                  | empty'''

def p_relleno(t):
    '''relleno : ID relleno
               | empty'''

def p_resultado(t):
    '''resultado : RESULT
                 | empty'''

def p_empty(p):
     'empty :'
     pass

def p_error(t):
    global aceptado
    aceptado = False
    print('Input RECHAZADO')
    print("Syntax error at '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()

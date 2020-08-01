import re
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

precedence = (
    ('left', 'LPAREN', 'LKEY'),
    ('left', 'ID'),
)

last_play = None
max_nested_level = 0
plays = {}

def p_s(t):
    's : game'
    global plays
    global last_play
    global max_nested_level
    res =  (last_play, plays[last_play])
    for x in plays:
        if plays[x] > res[1]:
            res = (x, plays[x])
    print('La primer jugada mas hecha en la serie es: ', res[0])
    print('Maximo nivel de anidamiento con una jugada dentro es: ', max_nested_level)
    plays = {}
    last_play = None


def p_game_empty(t):
    'game : metadata mov_1 result game'
    global plays
    global last_play
    if not (last_play in plays):
        plays[last_play] = 1
    else:
        plays[last_play] +=1

def p_game_fill(t):
    'game : empty'
    
def p_metadata(t):
    '''metadata : LBRACKET comm_fill_1 RBRACKET metadata
                | empty'''

def p_mov_1_fill(t):
    'mov_1 : sep_1 MOVEMENT comment_0 mov_2'
    global last_play
    last_play = t[2]

def p_mov_1_empty(t):
    'mov_1 : empty'

def p_sep_1(t):
    '''sep_1 : DOTS
             | TDOTS'''

def p_comment_0(t):
    'comment_0 : comment_1'
    global max_nested_level
    max_nested_level = t[1] if t[1] > max_nested_level else max_nested_level

def p_comment_0_empty(t):
    'comment_0 : empty'

def p_comment_1(t):
    '''comment_1 : LPAREN comm_fill_1 RPAREN
                 | LKEY comm_fill_1 RKEY'''
    t[0] = t[2]


def p_mov_2_fill(t):
    'mov_2 : MOVEMENT comment_0 mov_1'

def p_mov_2_empty(t):
    'mov_2 : empty'


def p_comm_fill_1_token(t):
    'comm_fill_1 : tok comm_fill_1'
    if t[1] > t[2]:
        t[0] = t[1]
    else:
        t[0] = t[2]


def p_comm_fill_1_comment(t):
    'comm_fill_1 : comment_1 comm_fill_1'
    if t[1] > t[2]:
        t[0] = t[1] + 1
    else: 
        t[0] = t[2]

def p_comm_fill_1_empty(t):
    'comm_fill_1 : empty'
    t[0] = 0

def p_tok_id(t):
    'tok : ID'
    t[0] = 0

def p_tok_mov(t):
    'tok : MOVEMENT'
    t[0] = 1

def p_tok_sep(t):
    'tok : sep_1'
    t[0] = 0

def p_result(t):
    '''result : RESULT
              | empty'''

def p_empty(p):
     'empty :'
     pass

def p_error(t):
    global aceptado
    aceptado = False
    print('Input RECHAZADO')

import ply.yacc as yacc
parser = yacc.yacc()

import re
aceptado = True
error = None


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
    r'([a-z]|[A-Z]|\d|"|:|-|\.|<|>|\*|\_|\?|\/|ó|í|\+)+'
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
    if error:
        return
    if last_play == None:
        print('No hubo jugadas')
        return
    res =  (last_play, plays[last_play])
    for x in plays:
        if plays[x] > res[1]:
            res = (x, plays[x])
    print(' > Primer jugada más frecuente: ', res[0])
    print(' > Comentario con jugada más anidado: ', max_nested_level, '\n')
    plays = {}
    last_play = None

def p_game_fill(t):
    'game : metadata mov_1 result game'
    global plays
    global last_play
    if not (last_play in plays):
        plays[last_play] = 1
    else:
        plays[last_play] +=1

def p_game_empty(t):
    'game : empty'
    
def p_metadata(t):
    '''metadata : LBRACKET fill RBRACKET metadata
                | empty'''

def p_mov_1_fill(t):
    'mov_1 : sep_1 MOVEMENT comment_chain mov_2'
    global last_play
    last_play = t[2]

def p_mov_1_empty(t):
    'mov_1 : empty'

def p_sep_1(t):
    '''sep_1 : DOTS
             | TDOTS'''

def p_comment_chain(t):
    'comment_chain : comment comment_chain'
    global max_nested_level
    incoming_max = t[1] if t[1] > t[2] else t[2]
    max_nested_level = incoming_max if incoming_max > max_nested_level else max_nested_level
    t[0] = max_nested_level

def p_comment_chain_empty(t):
    'comment_chain : empty'
    t[0] = 0

def p_comment(t):
    '''comment : LPAREN fill RPAREN
                 | LKEY fill RKEY'''
    t[0] = t[2]


def p_mov_2_fill(t):
    'mov_2 : MOVEMENT comment_chain mov_1'

def p_mov_2_empty(t):
    'mov_2 : empty'


def p_fill_token(t):
    'fill : tok fill'
    if t[1] > t[2]:
        t[0] = t[1]
    else:
        t[0] = t[2]


def p_fill_comment(t):
    'fill : comment fill'
    if t[1] >= t[2]:
        t[0] = t[1] + 1
    else: 
        t[0] = t[2]

def p_fill_empty(t):
    'fill : empty'
    t[0] = 0

def p_tok_id(t):
    'tok : ID'
    t[0] = 0

def p_tok_result(t):
    'tok : RESULT'
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
    global error
    aceptado = False
    if not error:
        error = t

import ply.yacc as yacc
parser = yacc.yacc()
aceptado = True
tokens = (
    'ATOKEN', 'BTOKEN'
    )

t_ATOKEN  = r'a'
t_BTOKEN  = r'b'



# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

def p_statementprima_print(t):
    'statementprima : statement'
    print('K es igual a : ', str(t[1]))

def p_statement_assign(t):
    'statement : ATOKEN statement BTOKEN'
    t[0] = t[2] + 1

def p_statement_expr(t):
    'statement : empty'
    t[0] = 0
    pass
 
def p_empty(p):
     'empty :'
     pass

def p_error(t):
    global aceptado
    aceptado = False
    print('Input RECHAZADO')
    # print("Syntax error at '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()


while True:
    try:
        aceptado = True
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
    if aceptado:
      print('Input ACEPTADO')
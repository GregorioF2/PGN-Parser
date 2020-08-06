import pgn_parser as tp
import argparse
import games


parser = argparse.ArgumentParser(description='Script runner.')  
parser.add_argument('-ls', '--live_stream', action="store_true", help= 'Si qres testear el parser con live stream input')
parser.add_argument('-t1', '--test_1', action="store_true", help='Correr parser para full game Hikaru Magnus')
parser.add_argument('-t2', '--test_2', action="store_true", help='Correr parser para small test y nested comments')
parser.add_argument('-t3', '--test_3', action="store_true", help='Correr parser para multiples partidas')
parser.add_argument('-t4', '--test_4', action="store_true", help='Correr parser para partida de chess.com')
parser.add_argument('-t5', '--test_5', action="store_true", help='Correr parser para historial de partidas chess.com')
parser.add_argument('-t6', '--test_6', action="store_true", help='Brackets de metadata desbalanceados')
parser.add_argument('-a', '--all', action='store_true', help='Correr todos los test juntos')
args = parser.parse_args()

print('====================\n')

def runParser(s):
  tp.aceptado = True
  tp.error = None
  tp.max_nested_level = 0

  tp.parser.parse(s)
  if tp.aceptado:
    print('Input ACEPTADO')
  else:
    print('Input RECHAZADO')
    print('Error: ', tp.error)
  
  print('\n====================\n')

def liveStream():
  while True:
    try:
      s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    runParser(s)

def printExpectedResults(test):
  print('Resultados esperados:')
  print('')
  if test['must_fail']:
    print( ' > Input debe ser rechazado')
  else:
    print(' > Primer jugada más frecuente: ', test['common_play'])
    print(' > Comentario con jugada más anidado: ', str(test['nested_comment']))
  print('')
  print('Resultados obtenidos:\n')

def test1FullGame():
  print('TEST #1 :> Partida completa Hikaru Magnus\n')
  printExpectedResults(games.full_game_hikaru_magnus)
  runParser(games.full_game_hikaru_magnus['game'])

def test2NestedComment():
  print('TEST #2 :> Partida chica comentarios anidados\n')
  printExpectedResults(games.small_game_three_coments_nested)
  runParser(games.small_game_three_coments_nested['game'])

def test3MultipleGames():
  print('TEST #3 :> Multiples partidas\n')
  printExpectedResults(games.multiple_games)
  runParser(games.multiple_games['game'])

def test4GameOfChessDotCom():
  print('TEST #4 :> Partida descargada de chess.com\n')
  printExpectedResults(games.game_of_chess_dot_com)
  runParser(games.game_of_chess_dot_com['game'])

def test5GamesChessDotCom():
  print('TEST #5 :> Hisorial de partidas chess.com\n')
  printExpectedResults(games.games_history_downloaded_chess_dot_com)
  runParser(games.games_history_downloaded_chess_dot_com['game'])

def test6UnbalancedBracketsMetadata():
  print('TEST #6 :> Brackets metadata desbalanceados')
  printExpectedResults(games.unbalanced_brackets)
  runParser(games.unbalanced_brackets['game'])

if args.live_stream:
  liveStream()
if args.test_1 or args.all:
  test1FullGame()
if args.test_2 or args.all:
  test2NestedComment()
if args.test_3 or args.all:
  test3MultipleGames()
if args.test_4 or args.all:
  test4GameOfChessDotCom()
if args.test_5 or args.all:
  test5GamesChessDotCom()
if args.test_6 or args.all:
  test6UnbalancedBracketsMetadata()
import pgn_parser as tp
import argparse
import games


parser = argparse.ArgumentParser(description='Script runner.')  
parser.add_argument('-ls', '--live_stream', action="store_true", help= 'Si qres testear el parser con live stream input')
parser.add_argument('-t1', '--test_1', action="store_true", help='Correr parser para full game Hikaru Magnus')
parser.add_argument('-t2', '--test_2', action="store_true", help='Correr parser para small test y nested comments')
parser.add_argument('-t3', '--test_3', action="store_true", help='Correr parser para multiples partidas')
args = parser.parse_args()


def runParser(s):
  tp.aceptado = True
  tp.parser.parse(s)
  if tp.aceptado:
    print('Input ACEPTADO')

def liveStream():
  while True:
    try:
      s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    runParser(s)

def test1FullGame():
  runParser(games.full_game_hikaru_magnus)

def test2NestedComment():
  runParser(games.small_game_three_coments_nested)

def test3MultipleGames():
  runParser(games.multiple_games)

if args.live_stream:
  liveStream()
if args.test_1:
  test1FullGame()
if args.test_2:
  test2NestedComment()
if args.test_3:
  test3MultipleGames()